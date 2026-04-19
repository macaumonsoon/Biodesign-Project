export function initEthicsPage() {
  const budget = document.getElementById("budget");
  const risk = document.getElementById("risk");
  const bv = document.getElementById("budget-value");
  const rv = document.getElementById("risk-value");
  const out = document.getElementById("ethics-output");

  const update = () => {
    bv.textContent = budget.value;
    rv.textContent = risk.value;
    const b = Number(budget.value);
    const r = Number(risk.value);
    if (b > 65 && r > 55) {
      out.textContent =
        "高去灭绝投入 + 高不确定性容忍：反思提示——哪些原住民主权与技术护栏应被视为不可谈判底线？";
    } else if (b < 35 && r < 40) {
      out.textContent =
        "保护优先路径：反思提示——即便不做复活，「灭绝记忆」的伦理工作是否仍不可缺席？";
    } else {
      out.textContent =
        "平衡策略：反思提示——公众沟通中，哪些未知应以「结构化不确定度」被显式呈现？";
    }
  };
  budget.addEventListener("input", update);
  risk.addEventListener("input", update);
  update();

  const input = document.getElementById("reflection-input");
  const save = document.getElementById("save-reflection");
  const load = document.getElementById("load-reflection");
  const status = document.getElementById("reflection-status");
  const key = "umwelt_archive_reflection_xr";

  save.addEventListener("click", () => {
    localStorage.setItem(key, input.value || "");
    status.textContent = "已保存到本地浏览器。";
  });
  load.addEventListener("click", () => {
    input.value = localStorage.getItem(key) || "";
    status.textContent = "已载入上次记录。";
  });
}
