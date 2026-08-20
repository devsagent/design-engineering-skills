# Research notes and provenance

These sources are references for explanatory design, not drop-in libraries. Reproduce principles, not distinctive assets or article-specific code.

The distributed React and CSS templates are original to this skill and are covered by this repository's MIT license. No upstream source code or visual assets are redistributed. The upstream licenses cited below apply to those upstream works, not automatically to these templates. If future revisions adapt upstream code or assets, record copyright, license, NOTICE, modifications, and source path explicitly.

## Thariq Shihipar: HTML Effectiveness

Studied source:

- Gallery: https://thariqs.github.io/html-effectiveness/#design
- Repository snapshot: https://github.com/ThariqS/html-effectiveness/tree/1787245d94aa680edf18b52027e3f859032776ba
- Animation prototype: https://thariqs.github.io/html-effectiveness/07-prototype-animation.html
- SVG figure sheet: https://thariqs.github.io/html-effectiveness/10-svg-illustrations.html
- Flowchart: https://thariqs.github.io/html-effectiveness/13-flowchart-diagram.html
- Research concept explainer: https://thariqs.github.io/html-effectiveness/15-research-concept-explainer.html
- License: Apache-2.0 at the studied snapshot: https://github.com/ThariqS/html-effectiveness/blob/1787245d94aa680edf18b52027e3f859032776ba/LICENSE

### Observed

The project is a set of self-contained HTML documents with no shared framework, build system, or maintained package API. Its README warns that examples are not maintained.

Repeated visual grammar:

- warm paper or restrained dark field;
- serif conceptual headings;
- system sans explanation;
- monospace timings, IDs, state, and code;
- clay/orange focus;
- olive success;
- rust failure;
- neutral borders and surfaces;
- generous spacing and concise labels.

Repeated authoring grammar:

1. State one question in prose.
2. Place the figure directly beside the claim.
3. Expose a small set of controls or selectable states.
4. Show the consequence immediately.
5. Add a caption, comparison, inspector, glossary, or source snippet.
6. Keep the artifact portable and directly inspectable.

The animation prototype separates tuning from the production figure. It exposes range controls, timing values, easing, replay, a visual keyframe track, and copy-ready output.

The figure sheet compares a family of visual metaphors on one surface. Its value is consistency review: stroke weights, semantic colors, label density, and export framing can be judged together.

The concept explainer connects animated geometry, controls, readouts, definitions, and a supporting table. The glossary is visible instead of tooltip-gated.

The flowchart uses selectable nodes, a detail pane, semantic branch colors, and directional connectors. The inspected source did not match every animation claim made by the gallery index, so verify current behavior rather than trusting promotional copy.

### Adapt

- self-contained executable editorial artifacts;
- motion tuning before production integration;
- visible glossary linked to figure regions;
- compact readouts beside causal controls;
- figure sheets as visual regression tools;
- short copy and explicit semantic color.

### Avoid

- copying standalone HTML assumptions into React;
- treating the gallery as a maintained component system;
- relying on autoplay;
- assuming every index description matches current source behavior;
- tiny SVG labels after responsive scaling;
- unqualified CSS selectors from isolated documents.

## Plannotator: effective-svg

Studied source:

- Repository snapshot: https://github.com/plannotator/effective-svg/tree/1d261aa176981467412f5ce1fe7aab810d105cf8
- License: MIT at the studied snapshot: https://github.com/plannotator/effective-svg/blob/1d261aa176981467412f5ce1fe7aab810d105cf8/LICENSE

### Observed

The snapshot contains documentation plus paired static and animated SVG files. It has no React or TypeScript source, package manifest, lockfile, install script, workflow, executable, release, or runtime dependency.

Source inspection found passive SVG/CSS assets rather than a software implementation. Animated files use embedded styles and named keyframes. Many contain detailed accessible labels and reduced-motion media queries.

### Security and provenance implications

Passive SVG is not automatically safe to inline. Audit:

- `<script>`;
- event attributes such as `onload`;
- `foreignObject`;
- external URLs;
- `javascript:` URLs;
- data URLs;
- embedded fonts;
- CSS imports;
- license and upstream design provenance.

Directly inlining multiple externally authored SVGs can cause collisions in:

- IDs;
- marker references;
- masks;
- gradients;
- filters;
- clip paths;
- global class selectors;
- keyframe names.

Namespace or translate every reusable internal identifier.

The repository license covers its contents, but its designs are derived from another project. Treat direct visual reuse as medium provenance risk unless the upstream chain is documented. Extract patterns instead of redistributing distinctive assets.

### Adapt

- paired static and motion variants;
- explicit reduced-motion rules;
- richly described SVG figures;
- restrained line-based technical metaphors;
- side-by-side visual review.

### Avoid

- treating it as a React library;
- bulk copying SVG files;
- preserving generic IDs or global CSS names;
- assuming repository license alone resolves upstream design provenance.

## Cursor: Git at any scale

Studied source:

- Article: https://cursor.com/blog/git-at-any-scale
- Studied from the live page and publicly delivered assets on 2026-08-19

### Observed diagram sequence

The article uses multiple custom diagrams as the narrative advances:

- a Git object walk with object and round-trip counters;
- logical object traversal correlated with physical packfile reads;
- a three-phase-commit explainer;
- replication with adjustable replica count and one-way latency;
- a write-ahead-log push sequence;
- two writers racing a conditional update, including a 412 response and retry;
- additional consistency and operational figures integrated with adjacent prose.

Common interaction model:

- a clear initial state;
- Back, Next, Reset, or Play controls;
- direct state selection where useful;
- visible counters and status labels;
- explicit failure states;
- motion that follows protocol order;
- article prose that introduces the exact question before the figure.

Common visual grammar:

- restrained neutral surfaces;
- sparse accent color;
- small monospace metadata;
- direct labels on nodes and edges;
- thin connectors;
- stateful stroke and fill changes;
- compact controls attached to the figure;
- visible captions and accessible names.

The figures teach effectively because they externalize hidden costs and protocol state. Round trips, acknowledgements, latency, retries, and conditional failures become observables rather than abstract prose.

### Adapt

- one protocol state per beat;
- counters tied to the same state model as the geometry;
- explicit failure and retry branches;
- user-controlled progression;
- prose and figure designed as one explanatory unit;
- responsive simplification rather than indiscriminate shrinking.

### Avoid

- ambient looping motion inside technical figures;
- counters driven independently from the visual state;
- revealing the full graph before the reader has context;
- hiding failures to keep a clean happy path;
- copying article-specific styling or source code.

## Synthesis

The shared lesson is not a particular SVG style. It is an authoring system:

```text
Claim in prose
→ static visual truth
→ one controllable variable or branch
→ immediate geometric change
→ literal readout
→ concise implication
→ inspectable tuning and export artifacts
```

Use that sequence as the default architecture for new explainers.
