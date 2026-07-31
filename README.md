# Design Engineering Skills

Two opinionated agent skills for designing and shipping high-craft web interfaces.

They combine product thinking, visual systems, interaction design, frontend engineering, accessibility, performance, and real browser verification into a focused workflow an agent can follow from brief to release.

## Skills

| Skill | Use it for |
| --- | --- |
| [`web-design`](skills/web-design/SKILL.md) | Choosing a visual direction, applying product-specific taste, rejecting generic AI/template defaults, building a coherent design system, designing responsive states, and reviewing interface craft. |
| [`frontend-development`](skills/frontend-development/SKILL.md) | Implementing or improving frontend code safely, preserving the existing stack, testing behavior, controlling performance, and verifying the finished interface in a real browser. |

The skills are complementary:

1. `web-design` decides what the interface should communicate and how it should feel.
2. `frontend-development` turns that direction into robust, accessible, verified software.

Use either one independently or load both for end-to-end design engineering.

## Install

Prerequisites:

- Node.js and npm for the `npx` installer.
- Python 3.9+ only when contributing or running repository validation.

Install the complete repository:

```bash
npx skills@latest add devsagent/design-engineering-skills
```

The repository follows the common `skills/<name>/SKILL.md` layout. To install manually, copy the complete `skills/web-design/` and/or `skills/frontend-development/` directory into your agent's documented skills directory. Keep each `SKILL.md` at the root of its named skill directory.

## What makes this system different

- **Brief before aesthetic.** The product, audience, task, and constraints determine the direction.
- **Systems before decoration.** Typography, spacing, color, shape, and motion are locked into a coherent language.
- **Specific over generic.** No automatic bento grids, gradient blobs, fake dashboards, or startup-copy filler.
- **Taste is a process.** Product truth, a recognition anchor, pattern budgets, subtraction, and adversarial tests prevent polished-but-interchangeable output.
- **States are part of the design.** Loading, empty, error, focus, hover, active, disabled, and success states are first-class work.
- **Motion must earn its place.** It clarifies hierarchy, feedback, continuity, or causality—or it is removed.
- **Accessibility is structural.** Semantic HTML, keyboard paths, focus behavior, contrast, reduced motion, and touch targets are designed in.
- **Verification is visible.** A passing build is necessary but never substitutes for responsive browser QA and interaction checks.

## Example prompts

### Design a new surface

```text
Use the web-design skill to define and design a focused landing page for this product.
Start with a design read, choose the system locks, and explain the mobile collapse before implementation.
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

### Improve an existing interface

```text
Use both skills to audit and improve this interface.
Preserve the product's identity and information architecture, prioritize the highest-impact problems, implement focused changes, and show real verification evidence.
```

### Review a pull request

```text
Review this frontend diff with both skills.
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
    ├── frontend-development/
    │   └── SKILL.md
    └── web-design/
        ├── SKILL.md
        └── references/
            └── taste-and-anti-slop.md
```

## Validation

Run the dependency-free validator and its regression tests:

```bash
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests -v
```

The validator checks directory names, required frontmatter, description length, file size, non-empty bodies, metadata nesting, and related-skill references. To stay dependency-free, repository manifests use a strict YAML subset: top-level scalar fields, a two-space-indented `metadata` mapping, and inline string lists for `tags` and `related_skills`. The validator rejects duplicate keys, malformed lists, unknown fields, invalid quoting, and unsupported nesting.

## Contributing

Keep additions behavioral and testable. A useful rule changes what an agent does, identifies when it applies, and ends with evidence that proves the work is complete. Avoid vague advice, duplicated checklists, personal project conventions, framework lock-in, and aesthetic rules presented as universal truth.

## License

MIT
