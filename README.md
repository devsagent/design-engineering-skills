# Design Engineering Skills

Three opinionated agent skills for designing interfaces, shipping frontend software, and art-directing distinctive editorial covers.

They combine product thinking, visual systems, interaction design, frontend engineering, accessibility, performance, image-generation discipline, and real browser verification into focused workflows an agent can follow from brief to release.

## Skills

| Skill | Use it for |
| --- | --- |
| [`web-design`](skills/web-design/SKILL.md) | Choosing a visual direction, applying product-specific taste, rejecting generic AI/template defaults, designing route-backed master-detail content experiences, building a coherent system, and reviewing responsive interface craft. |
| [`frontend-development`](skills/frontend-development/SKILL.md) | Implementing or improving frontend code safely, preserving the existing stack, testing behavior, controlling performance, and verifying the finished interface in a real browser. |
| [`dotted-painterly-cover-art`](skills/dotted-painterly-cover-art/SKILL.md) | Creating native-raster editorial covers with painterly massing and form-modeling square-cell stippling, including concept selection, prompts, exclusions, crop QA, replacement workflows, and publication verification. |

The skills are complementary:

1. `web-design` decides what the interface should communicate and how it should feel.
2. `frontend-development` turns that direction into robust, accessible, verified software.
3. `dotted-painterly-cover-art` directs and verifies a specialized generated-image system when editorial imagery needs that visual language.

Use any skill independently or combine them for end-to-end design engineering.

## Install

Prerequisites:

- Node.js and npm for the `npx` installer.
- Python 3.9+ only when contributing or running repository validation.

Install the complete repository:

```bash
npx skills@latest add devsagent/design-engineering-skills
```

The repository follows the common `skills/<name>/SKILL.md` layout. To install manually, copy the complete directory for any desired skill into your agent's documented skills directory. Keep each `SKILL.md` at the root of its named skill directory and preserve linked `references/` files.

## What makes this system different

- **Brief before aesthetic.** The product, audience, task, and constraints determine the direction.
- **Systems before decoration.** Typography, spacing, color, shape, motion, and image grammar are locked into coherent languages.
- **Specific over generic.** No automatic bento grids, gradient blobs, fake dashboards, blue network graphs, or startup-copy filler.
- **Taste is a process.** Product truth, a recognition anchor, pattern budgets, subtraction, and adversarial tests prevent polished-but-interchangeable output.
- **Information architecture before panes.** Collection, list, detail, route, and mobile semantics precede a three-column master-detail frame.
- **States are part of the design.** Loading, empty, error, focus, hover, active, selected, disabled, and success states are first-class work.
- **Motion must earn its place.** It clarifies hierarchy, feedback, continuity, or causality, or it is removed.
- **Accessibility is structural.** Semantic HTML, keyboard paths, focus behavior, contrast, reduced motion, and touch targets are designed in.
- **Generated images are artifacts, not prompts.** A real native raster, tested crops, strict exclusions, deterministic text policy, and production bytes are required.
- **Verification is visible.** A passing build is necessary but never substitutes for responsive browser QA, interaction checks, or inspection of final pixels.

## Example prompts

### Design a new surface

```text
Use the web-design skill to define and design a focused landing page for this product.
Start with a design read, choose the system locks, and explain the mobile collapse before implementation.
```

### Design a Notes-style master-detail experience

```text
Use the web-design skill and its master-detail-content-ux reference.
Define the collection, row, typed-detail, route, aggregate, focus, and mobile Back contracts before drawing the desktop panes. Then verify direct loads, browser history, selected-row continuity, 320px/375px behavior, and long detail content.
```

### Prevent a generic result

```text
Use the web-design skill and its taste-and-anti-slop reference.
Name the obvious template completion, define the product truth and recognition anchor, reject unsupported defaults, and run the swap, subtraction, truth, edge-state, and memory tests before shipping.
```

### Build the design

```text
Use the frontend-development skill to implement the approved design in the existing stack.
Preserve current behavior, cover all UI states, and verify it at mobile, tablet, and desktop widths.
```

### Create a dotted painterly cover

```text
Use the dotted-painterly-cover-art skill to create a textless native-raster cover for this article.
Choose one physical metaphor, preserve the approved palette and form-modeling square-cell texture, explicitly ban generic network-graph cues, and inspect the full image plus every real card, mobile, and social crop before integrating it.
```

### Improve an existing interface

```text
Use web-design and frontend-development to audit and improve this interface.
Preserve the product's identity and information architecture, prioritize the highest-impact problems, implement focused changes, and show real verification evidence.
```

### Review a pull request

```text
Review this frontend diff with web-design and frontend-development.
Separate functional, accessibility, responsive, performance, and craft findings. Cite exact files and lines, then give an explicit ship verdict.
```

## Repository structure

```text
.
├── README.md
├── LICENSE
├── scripts/
│   └── validate_skills.py
├── tests/
│   └── test_validate_skills.py
└── skills/
    ├── dotted-painterly-cover-art/
    │   └── SKILL.md
    ├── frontend-development/
    │   └── SKILL.md
    └── web-design/
        ├── SKILL.md
        └── references/
            ├── master-detail-content-ux.md
            └── taste-and-anti-slop.md
```

## Validation

Run the dependency-free validator and its regression tests:

```bash
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests -v
```

The validator checks directory names, required frontmatter, description length, file size, non-empty bodies, metadata nesting, related-skill references, and README indexing. To stay dependency-free, repository manifests use a strict YAML subset: top-level scalar fields, a two-space-indented `metadata` mapping, and inline string lists for `tags` and `related_skills`. Frontmatter uses ASCII spaces only; tabs, non-ASCII whitespace, control characters, duplicate keys or list values, malformed lists, unknown fields, invalid quoting, and unsupported nesting are rejected. Tags and related-skill names use lowercase kebab case.

## Contributing

Keep additions behavioral and testable. A useful rule changes what an agent does, identifies when it applies, and ends with evidence that proves the work is complete. Avoid vague advice, duplicated checklists, personal project conventions, framework lock-in, and aesthetic rules presented as universal truth.

## License

MIT
