import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import { VRButton } from "three/addons/webxr/VRButton.js";
import { ARButton } from "three/addons/webxr/ARButton.js";
import {
  loadDataset,
  buildArchivalMap,
  speciesToPoints,
  latLonToPosition,
  categoryColorHex,
  getSpeciesLink,
  PORTAL_LABELS
} from "./xr-data.js";

const GLOBE_RADIUS = 1;
const MARKER_RADIUS = 0.022;

const REGION_PRESETS = {
  global: { lat: 12, lon: 25, dist: 2.85, polar: 0.52 },
  asia: { lat: 35, lon: 95, dist: 2.1, polar: 0.35 },
  europe: { lat: 52, lon: 18, dist: 2.05, polar: 0.32 },
  africa: { lat: 2, lon: 20, dist: 2.15, polar: 0.38 },
  nam: { lat: 40, lon: -98, dist: 2.05, polar: 0.34 },
  sam: { lat: -18, lon: -62, dist: 2.1, polar: 0.36 },
  arctic: { lat: 72, lon: -40, dist: 2.25, polar: 0.42 },
  antarctic: { lat: -78, lon: 0, dist: 2.35, polar: 0.48 }
};

function makeMeridianParallels(radius, divisionsLat = 12, divisionsLon = 24) {
  const material = new THREE.LineBasicMaterial({
    color: 0xa8b8d0,
    transparent: true,
    opacity: 0.22
  });
  const group = new THREE.Group();

  for (let i = 0; i <= divisionsLon; i++) {
    const lon = -180 + (360 / divisionsLon) * i;
    const pts = [];
    for (let j = 0; j <= 64; j++) {
      const lat = -85 + (170 / 64) * j;
      const v = new THREE.Vector3();
      latLonToPosition(lat, lon, radius, v);
      pts.push(v);
    }
    const geom = new THREE.BufferGeometry().setFromPoints(pts);
    group.add(new THREE.Line(geom, material));
  }

  for (let i = 0; i <= divisionsLat; i++) {
    const lat = -80 + (160 / divisionsLat) * i;
    const pts = [];
    for (let j = 0; j <= 96; j++) {
      const lon = -180 + (360 / 96) * j;
      const v = new THREE.Vector3();
      latLonToPosition(lat, lon, radius, v);
      pts.push(v);
    }
    const geom = new THREE.BufferGeometry().setFromPoints(pts);
    group.add(new THREE.Line(geom, material));
  }
  return group;
}

function continentLabels(radius) {
  const group = new THREE.Group();
  const canvasTex = (text) => {
    const c = document.createElement("canvas");
    c.width = 512;
    c.height = 128;
    const ctx = c.getContext("2d");
    ctx.fillStyle = "rgba(240,245,255,0.55)";
    ctx.font = "bold 44px Georgia, 'Noto Serif SC', serif";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(text, 256, 64);
    const tex = new THREE.CanvasTexture(c);
    tex.colorSpace = THREE.SRGBColorSpace;
    return tex;
  };

  const labels = [
    { t: "NORTH AMERICA", lat: 38, lon: -100 },
    { t: "SOUTH AMERICA", lat: -23, lon: -62 },
    { t: "EUROPE", lat: 51, lon: 12 },
    { t: "ASIA", lat: 33, lon: 90 },
    { t: "AFRICA", lat: 5, lon: 18 },
    { t: "ATLANTIC", lat: 10, lon: -35 },
    { t: "PACIFIC", lat: 5, lon: 165 }
  ];

  labels.forEach(({ t, lat, lon }) => {
    const spriteMat = new THREE.SpriteMaterial({
      map: canvasTex(t),
      transparent: true,
      depthWrite: false,
      opacity: 0.85
    });
    const sprite = new THREE.Sprite(spriteMat);
    const p = new THREE.Vector3();
    latLonToPosition(lat, lon, radius * 1.02, p);
    sprite.position.copy(p);
    const s = 0.35;
    sprite.scale.set(s * 2.2, s * 0.55, 1);
    group.add(sprite);
  });
  return group;
}

function greatCircleArc(p1, p2, radius, segments = 32) {
  const v1 = p1.clone().normalize();
  const v2 = p2.clone().normalize();
  const pts = [];
  for (let i = 0; i <= segments; i++) {
    const t = i / segments;
    const v = new THREE.Vector3().copy(v1).lerp(v2, t).normalize().multiplyScalar(radius * 1.008);
    pts.push(v);
  }
  const geom = new THREE.BufferGeometry().setFromPoints(pts);
  return new THREE.Line(
    geom,
    new THREE.LineBasicMaterial({ color: 0xc8b070, transparent: true, opacity: 0.35 })
  );
}

export async function initGlobe() {
  const canvas = document.getElementById("xr-canvas");
  const chipCount = document.getElementById("xr-species-count");
  const card = document.getElementById("xr-species-card");
  const cardBody = document.getElementById("xr-card-body");
  const cardClose = document.getElementById("xr-card-close");
  const tooltip = document.getElementById("xr-tooltip");
  const xrSlot = document.getElementById("xr-webxr-slot");

  const { species, archival } = await loadDataset();
  const archivalMap = buildArchivalMap(archival);
  const points = speciesToPoints(species);
  if (chipCount) {
    chipCount.textContent = `${species.length} 灭绝物种 · Destinations`;
  }

  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x030508);

  const starsGeom = new THREE.BufferGeometry();
  const starPositions = [];
  for (let i = 0; i < 1600; i++) {
    const r = 12 + Math.random() * 28;
    const θ = Math.random() * Math.PI * 2;
    const φ = Math.acos(2 * Math.random() - 1);
    starPositions.push(
      r * Math.sin(φ) * Math.cos(θ),
      r * Math.sin(φ) * Math.sin(θ),
      r * Math.cos(φ)
    );
  }
  starsGeom.setAttribute("position", new THREE.Float32BufferAttribute(starPositions, 3));
  scene.add(
    new THREE.Points(
      starsGeom,
      new THREE.PointsMaterial({ color: 0xb8c8e8, size: 0.02, transparent: true, opacity: 0.45 })
    )
  );

  const camera = new THREE.PerspectiveCamera(48, 1, 0.05, 200);
  camera.position.set(0, 0.35, 2.9);

  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: false });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.05;
  renderer.xr.enabled = true;

  const hemi = new THREE.HemisphereLight(0x9db4ff, 0x080a10, 0.55);
  scene.add(hemi);
  const dir = new THREE.DirectionalLight(0xfff2dd, 0.85);
  dir.position.set(3.5, 2.2, 2.5);
  scene.add(dir);

  const earthGroup = new THREE.Group();
  scene.add(earthGroup);

  const globeGeo = new THREE.SphereGeometry(GLOBE_RADIUS, 96, 64);
  const globeMat = new THREE.MeshStandardMaterial({
    color: 0x1a2432,
    roughness: 0.92,
    metalness: 0.08,
    emissive: new THREE.Color(0x05070a),
    emissiveIntensity: 0.4
  });
  const globe = new THREE.Mesh(globeGeo, globeMat);
  earthGroup.add(globe);

  const gridGroup = makeMeridianParallels(GLOBE_RADIUS * 1.001);
  earthGroup.add(gridGroup);

  const labelGroup = continentLabels(GLOBE_RADIUS * 1.015);
  earthGroup.add(labelGroup);

  const routesGroup = new THREE.Group();
  earthGroup.add(routesGroup);

  const markersGroup = new THREE.Group();
  earthGroup.add(markersGroup);

  const markerMeshes = [];
  const tmpVec = new THREE.Vector3();

  points.forEach((sp, i) => {
    latLonToPosition(sp.lat, sp.lon, GLOBE_RADIUS * 1.018, tmpVec);
    const geom = new THREE.SphereGeometry(MARKER_RADIUS, 10, 10);
    const mat = new THREE.MeshStandardMaterial({
      color: categoryColorHex(sp.category),
      emissive: new THREE.Color(categoryColorHex(sp.category)),
      emissiveIntensity: 0.25,
      roughness: 0.45,
      metalness: 0.15
    });
    const mesh = new THREE.Mesh(geom, mat);
    mesh.position.copy(tmpVec);
    mesh.userData.species = sp;
    mesh.userData.idx = i;
    markersGroup.add(mesh);
    markerMeshes.push(mesh);
  });

  function rebuildRoutes() {
    while (routesGroup.children.length) routesGroup.remove(routesGroup.children[0]);
    const byCat = new Map();
    points.forEach(p => {
      if (!byCat.has(p.category)) byCat.set(p.category, []);
      byCat.get(p.category).push(p);
    });
    let lines = 0;
    byCat.forEach(arr => {
      if (arr.length < 2) return;
      for (let i = 0; i < arr.length - 1 && lines < 36; i++) {
        const a = new THREE.Vector3();
        const b = new THREE.Vector3();
        latLonToPosition(arr[i].lat, arr[i].lon, GLOBE_RADIUS * 1.012, a);
        latLonToPosition(arr[i + 1].lat, arr[i + 1].lon, GLOBE_RADIUS * 1.012, b);
        routesGroup.add(greatCircleArc(a, b, GLOBE_RADIUS * 1.012));
        lines++;
      }
    });
  }
  rebuildRoutes();

  const controls = new OrbitControls(camera, canvas);
  controls.enableDamping = true;
  controls.dampingFactor = 0.06;
  controls.minDistance = 1.55;
  controls.maxDistance = 5.5;
  controls.rotateSpeed = 0.65;
  controls.zoomSpeed = 0.55;

  let autoRotate = true;
  let scatter = false;
  let migratePhase = 0;
  const basePositions = markerMeshes.map(m => m.position.clone());

  function resize() {
    const w = window.innerWidth;
    const h = window.innerHeight;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
  }
  resize();
  window.addEventListener("resize", resize);

  const raycaster = new THREE.Raycaster();
  const pointer = new THREE.Vector2();
  let hovered = null;

  function setRegion(key) {
    const p = REGION_PRESETS[key] || REGION_PRESETS.global;
    const target = new THREE.Vector3();
    latLonToPosition(p.lat, p.lon, 0.02, target);
    controls.target.copy(target);
    const camPos = new THREE.Vector3();
    latLonToPosition(p.lat + p.polar * 18, p.lon - 32, p.dist, camPos);
    camera.position.copy(camPos);
    controls.update();
  }

  document.querySelectorAll("[data-region]").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll("[data-region]").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      setRegion(btn.dataset.region);
    });
  });

  document.getElementById("xr-toggle-grid")?.addEventListener("change", e => {
    gridGroup.visible = e.target.checked;
  });
  document.getElementById("xr-toggle-routes")?.addEventListener("change", e => {
    routesGroup.visible = e.target.checked;
  });
  document.getElementById("xr-toggle-story")?.addEventListener("change", e => {
    labelGroup.visible = e.target.checked;
  });
  document.getElementById("xr-toggle-rotate")?.addEventListener("change", e => {
    autoRotate = e.target.checked;
  });
  document.getElementById("xr-toggle-scatter")?.addEventListener("change", e => {
    scatter = e.target.checked;
    if (!scatter) {
      markerMeshes.forEach((m, i) => m.position.copy(basePositions[i]));
    }
  });
  let migrateBurst = 0;
  document.getElementById("xr-btn-migrate")?.addEventListener("click", () => {
    migrateBurst = 100;
  });

  function portalLinksHtml(portalUrls = {}) {
    const keys = Object.keys(portalUrls);
    if (!keys.length) return "";
    return keys
      .slice(0, 4)
      .map(k => {
        const label = PORTAL_LABELS[k] || k;
        return `<a href="${portalUrls[k]}" target="_blank" rel="noopener">${label}</a>`;
      })
      .join("");
  }

  function showCard(sp) {
    const arch = archivalMap.get(sp.scientific_name);
    const portals = portalLinksHtml(arch?.portal_urls);
    cardBody.innerHTML = `
      <h3>${sp.common_name_zh || sp.common_name_en || sp.scientific_name}</h3>
      <div class="sci">${sp.common_name_en || ""} · ${sp.scientific_name}</div>
      <p class="meta">${sp.category} · ${sp.extinction_summary} · ${sp.region || ""}</p>
      <p class="meta">Sensory ${sp.sensory_reconstruction_score} · Music ${sp.music_layering_score} · Data ${sp.data_availability}</p>
      <p class="meta">${sp.extinction_drivers || ""}</p>
      <div class="actions">
        <a href="${getSpeciesLink(sp.slug)}">数字档案 Digital dossier</a>
        ${portals}
      </div>
    `;
    card.classList.add("visible");
  }

  cardClose?.addEventListener("click", () => card.classList.remove("visible"));

  canvas.addEventListener("pointermove", ev => {
    const rect = canvas.getBoundingClientRect();
    pointer.x = ((ev.clientX - rect.left) / rect.width) * 2 - 1;
    pointer.y = -((ev.clientY - rect.top) / rect.height) * 2 + 1;
    raycaster.setFromCamera(pointer, camera);
    const hits = raycaster.intersectObjects(markerMeshes, false);
    if (hits.length) {
      const sp = hits[0].object.userData.species;
      hovered = sp;
      tooltip.style.display = "block";
      tooltip.style.left = `${ev.clientX + 14}px`;
      tooltip.style.top = `${ev.clientY + 14}px`;
      tooltip.textContent = `${sp.common_name_zh || ""} / ${sp.common_name_en || sp.scientific_name}`;
    } else {
      hovered = null;
      tooltip.style.display = "none";
    }
  });

  canvas.addEventListener("click", () => {
    if (!hovered) return;
    showCard(hovered);
  });

  if (xrSlot) {
    const vrBtn = VRButton.createButton(renderer);
    vrBtn.title = "Enter VR (WebXR)";
    xrSlot.appendChild(vrBtn);
    try {
      const arBtn = ARButton.createButton(renderer);
      arBtn.title = "Enter AR (WebXR — device dependent)";
      xrSlot.appendChild(arBtn);
    } catch {
      /* AR optional */
    }
  }

  renderer.xr.addEventListener("sessionstart", () => {
    controls.enabled = false;
  });
  renderer.xr.addEventListener("sessionend", () => {
    controls.enabled = true;
  });

  function animate() {
    if (autoRotate && !renderer.xr.isPresenting) {
      earthGroup.rotation.y += 0.0009;
    }
    migratePhase += 0.012;
    if (scatter) {
      markerMeshes.forEach((m, i) => {
        const bp = basePositions[i];
        const nudge = 0.04 * Math.sin(migratePhase + i * 0.7);
        m.position.copy(bp).multiplyScalar(1 + nudge);
      });
    }
    if (migrateBurst > 0) {
      migrateBurst -= 1;
      earthGroup.rotation.y += 0.0055;
    }
    controls.update();
    renderer.render(scene, camera);
  }
  renderer.setAnimationLoop(animate);

  setRegion("global");
  document.querySelector('[data-region="global"]')?.classList.add("active");
}
