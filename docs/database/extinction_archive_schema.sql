-- Extinction Archive / Umwelt Archive — core DDL (PostgreSQL-oriented)
-- See extinction_archive_schema.md for rationale and CSV mapping.

CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TABLE taxonomic_group (
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  slug        text NOT NULL UNIQUE,
  label_en    text NOT NULL,
  label_zh    text,
  sort_order  int NOT NULL DEFAULT 0
);

CREATE TABLE taxon (
  id                              uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  scientific_name                 text NOT NULL UNIQUE,
  common_name_en                  text,
  common_name_zh                  text,
  taxonomic_group_id              uuid REFERENCES taxonomic_group (id),
  extinction_period_raw           text,
  extinction_year_ce              int,
  extinction_year_ce_upper        int,
  distribution_summary            text,
  extinction_drivers_summary      text,
  internal_notes                  text,
  sensory_potential_score         smallint CHECK (sensory_potential_score BETWEEN 0 AND 10),
  music_layering_potential_score  smallint CHECK (music_layering_potential_score BETWEEN 0 AND 10),
  data_availability               text NOT NULL CHECK (data_availability IN ('high', 'medium', 'low')),
  slug                            text NOT NULL UNIQUE,
  featured_rank                   int,
  flags                           jsonb DEFAULT '{}'::jsonb,
  created_at                      timestamptz NOT NULL DEFAULT now(),
  updated_at                      timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE geographic_site (
  id               uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  taxon_id         uuid NOT NULL REFERENCES taxon (id) ON DELETE CASCADE,
  site_role        text NOT NULL,
  label_en         text,
  label_zh         text,
  latitude         double precision,
  longitude        double precision,
  uncertainty_m    int,
  geojson          jsonb,
  epistemic_tier   text NOT NULL CHECK (epistemic_tier IN ('cited', 'interpolated', 'speculative')),
  source_note      text,
  citation_id      uuid
);

CREATE TABLE citation (
  id          uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  cite_key    text NOT NULL UNIQUE,
  apa_or_short text NOT NULL,
  url         text,
  bibtex      text
);

ALTER TABLE geographic_site
  ADD CONSTRAINT geographic_site_citation_fk
  FOREIGN KEY (citation_id) REFERENCES citation (id);

CREATE TABLE reconstruction_layer (
  id                 uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  taxon_id           uuid NOT NULL REFERENCES taxon (id) ON DELETE CASCADE,
  channel            text NOT NULL CHECK (channel IN (
                        'visual', 'auditory', 'olfactory', 'haptic', 'narrative', 'chronobiology'
                      )),
  epistemic_tier     text NOT NULL CHECK (epistemic_tier IN ('cited', 'interpolated', 'speculative')),
  title_en           text,
  title_zh           text,
  description_en     text,
  description_zh     text,
  data_proxy_summary text,
  default_intensity  numeric(3, 2) CHECK (default_intensity >= 0 AND default_intensity <= 1),
  enabled_by_default boolean NOT NULL DEFAULT true,
  sort_order         int NOT NULL DEFAULT 0
);

CREATE TABLE sonification_profile (
  id               uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  taxon_id         uuid NOT NULL UNIQUE REFERENCES taxon (id) ON DELETE CASCADE,
  stem_definitions jsonb NOT NULL DEFAULT '[]'::jsonb,
  mix_notes        text,
  bpm_min          int,
  bpm_max          int
);

CREATE TABLE media_asset (
  id              uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  taxon_id        uuid NOT NULL REFERENCES taxon (id) ON DELETE CASCADE,
  kind            text NOT NULL CHECK (kind IN (
                     'sketchfab', 'gltf', 'audio', 'image', 'video', 'document'
                   )),
  url             text NOT NULL,
  title           text,
  license         text,
  attribution     text,
  epistemic_tier  text CHECK (epistemic_tier IN ('cited', 'interpolated', 'speculative')),
  channel         text,
  is_primary      boolean NOT NULL DEFAULT false
);

CREATE TABLE taxon_citation (
  taxon_id    uuid NOT NULL REFERENCES taxon (id) ON DELETE CASCADE,
  citation_id uuid NOT NULL REFERENCES citation (id) ON DELETE CASCADE,
  context     text,
  PRIMARY KEY (taxon_id, citation_id)
);

CREATE TABLE experience_scene (
  id               uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  scene_id         text NOT NULL UNIQUE,
  taxon_id         uuid REFERENCES taxon (id) ON DELETE SET NULL,
  locale           text NOT NULL CHECK (locale IN ('en', 'zh')),
  title            text NOT NULL,
  body_markdown    text,
  reflection_prompt text,
  ethics_branch_id text
);

CREATE TABLE locale_string (
  key    text NOT NULL,
  locale text NOT NULL CHECK (locale IN ('en', 'zh')),
  value  text NOT NULL,
  PRIMARY KEY (key, locale)
);

CREATE INDEX idx_taxon_group ON taxon (taxonomic_group_id);
CREATE INDEX idx_taxon_data_availability ON taxon (data_availability);
CREATE INDEX idx_geographic_site_taxon ON geographic_site (taxon_id);
CREATE INDEX idx_media_taxon ON media_asset (taxon_id);
CREATE INDEX idx_layer_taxon ON reconstruction_layer (taxon_id);
