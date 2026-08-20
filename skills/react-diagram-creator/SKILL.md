---
name: react-diagram-creator
description: "Use when building, redesigning, or reviewing responsive technical diagrams, concept explainers, interactive flowcharts, SVG figure sheets, or animation sandboxes in React or Next.js. Covers explanatory state models, linked glossaries, semantic SVG, measurable controls, accessible motion, mobile topology, and verification."
version: 1.0.0
author: devsagent
license: MIT
metadata:
  tags: [react, diagrams, svg, data-visualization, accessibility, motion, responsive-design]
  related_skills: [web-design, frontend-development]
---

# React Diagram Creator

## Overview

Create technical diagrams as executable editorial documents. The goal is not to decorate a page. The goal is to make one relationship observable.

## When to Use

Use this skill for diagrams embedded in React applications, Next.js pages, technical articles, documentation, explainers, and product education. It is especially useful when the figure needs selectable states, deterministic controls, visible counters, linked glossary terms, failure branches, responsive topology, or restrained causal motion.

For general page hierarchy and visual direction, also use `web-design`. For production React architecture outside the figure itself, also use `frontend-development`.

## Core contract

Write these four lines before drawing:

```text
Question: What should the reader understand?
Variable: What can the reader change or inspect?
Observable: What visibly proves the relationship?
Implication: Why does the change matter?
```

If any line is vague, the diagram is not ready to build.

A strong diagram has:

- one primary claim;
- a complete, useful static state;
- controls only for variables that alter the lesson;
- immediate visual and textual consequences;
- semantic HTML around local SVG geometry;
- a responsive topology, not merely a scaled desktop canvas;
- a reduced-motion state that preserves all information;
- deterministic examples and honest readouts.

## Required workflow

### 1. Inspect before inventing

Audit the page and repository first:

1. Read framework and project instructions.
2. Find existing design tokens, fonts, layout wrappers, controls, figures, SVGs, and motion utilities.
3. Identify existing accessibility and reduced-motion conventions.
4. Check the target container width at desktop and mobile.
5. Decide what can be shared and what geometry must remain subject-specific.

Do not add a diagram library before proving the project needs one. Prefer a thin local substrate over a speculative DSL.

**Complete when:** existing primitives, tokens, container widths, motion utilities, and project constraints are recorded, with each proposed new abstraction justified.

### 2. Choose the explanatory archetype

Use the smallest pattern that answers the question:

| Pattern | Best for | Minimum interaction |
|---|---|---|
| Static figure | Structure, taxonomy, one stable comparison | None |
| Selectable concept map | Definitions and relationships | Select a term or region |
| Flow explorer | Ordered work, retries, failure branches | Back, next, reset, direct node selection |
| Parameter explainer | Rates, capacity, quorum, latency, tradeoffs | One or two bounded inputs plus live readouts |
| Comparison panel | Before/after or alternative architectures | Explicit state switch |
| Animation sandbox | Tuning timing, easing, choreography | Replay, duration, easing, reduced-motion preview |
| Figure sheet | Visual grammar, export crops, variants | Annotation or crop toggles only if useful |

Do not combine archetypes because the page feels empty. Add a second pattern only when it teaches a second relationship.

**Complete when:** one primary archetype is selected, rejected alternatives are noted, and its minimum interaction is explicit.

### 3. Choose the rendering medium

Use semantic HTML and CSS when:

- labels, cards, controls, and reading order dominate;
- layout should reflow naturally;
- nodes are interactive;
- native focus and text selection matter.

Use inline SVG when:

- connectors, paths, topology, or precise geometry dominate;
- vector export matters;
- the visual has a stable coordinate system;
- accessible `<title>` and `<desc>` can describe the figure.

Use a hybrid by default:

- HTML for headings, prose, controls, readouts, glossary, and detail panels;
- SVG for edges, paths, queues, timelines, and compact topology;
- CSS variables for theme and motion tuning;
- React state for semantic states, never for every animation frame.

Use Canvas only for dense continuous scenes where DOM or SVG becomes a measured bottleneck. Canvas requires a separate semantic representation.

**Complete when:** the rendering medium is chosen per layer and every Canvas layer has a documented semantic equivalent.

### 4. Build the static truth first

Before motion or controls:

1. Render the default state with JavaScript disabled where practical.
2. Make the title, labels, direction, terminal state, and implication readable.
3. Use visible text instead of tooltip-only meaning.
4. Encode status with at least two channels, such as color plus label, icon, stroke, or pattern.
5. Keep decorative paths out of the accessibility tree.
6. Write a literal text description of the topology and current values.

If a screenshot cannot teach the basic claim, motion will not rescue it.

**Complete when:** a static screenshot communicates the entities, direction, current state, terminal or comparison state, and implication without hover or autoplay.

### 5. Model interaction as a small state machine

Use named domain states, not scattered booleans.

```ts
type DiagramState =
  | { phase: "ready" }
  | { phase: "accepted" }
  | { phase: "processing" }
  | { phase: "complete"; outcome: "success" }
  | { phase: "complete"; outcome: "retry" };
```

For step-based figures, define data first:

```ts
type Step = {
  id: string;
  label: string;
  role: string;
  status: string;
  explanation: string;
};
```

Then derive:

- active node;
- completed nodes;
- current connector state;
- detail panel copy;
- live status;
- enabled and disabled controls;
- literal accessibility description.

Required controls for a manually stepped sequence:

- Previous;
- Next;
- Reset;
- direct node selection when nodes are visible;
- explicit failure or alternate-state toggles when the branch is part of the lesson.

Add Play or Pause only when timing or autonomous progression teaches something. Default autoplay off. Never make autoplay the only way to understand the sequence.

**Complete when:** one typed model derives geometry, readout, implication, motion frame, and accessible description, with no impossible state combinations. See [`templates/causal-flow-example.tsx`](templates/causal-flow-example.tsx).

### 6. Make concept explainers measurable

A concept explainer needs more than highlighted boxes.

1. Define one causal model.
2. Expose no more than two primary inputs at once.
3. Derive all outputs from those inputs.
4. Show both the system and the resulting measurements.
5. Link glossary terms to visible regions.
6. Keep definitions visible; hover may supplement but never gate them.
7. Make examples deterministic.
8. Label simulation windows, assumptions, and units.
9. Calibrate defaults so the initial state teaches the intended relationship.
10. Explain surprising outliers instead of hiding them.

A finite queue example should distinguish temporary capacity from throughput. A quorum example should distinguish replica count from required acknowledgements. A retry example should preserve request identity across attempts.

**Complete when:** boundary, balanced, overloaded or failure, and terminal inputs produce independently checked values, and glossary selection locates the same concepts in the figure.

### 7. Add motion only for causality

Motion may communicate:

- direction;
- order;
- transfer;
- branching;
- accumulation;
- acknowledgement;
- retry;
- state settlement.

Do not animate for atmosphere inside a technical figure.

Build and tune motion in isolation:

- replay the same transition;
- expose duration and easing options;
- show labeled keyframes or phases;
- avoid layout shifts;
- compare the normal and reduced-motion outcomes;
- move the chosen values into the production figure only after review.

Starting ranges:

- local acknowledgement: 140–220ms;
- node or panel transition: 220–420ms;
- multi-stage explanatory sequence: 500–900ms;
- autoplay step dwell: 900–1600ms.

Use these only as starting points. Timing follows information density.

Pause autonomous playback when:

- the document is hidden;
- the figure is offscreen;
- the user presses pause;
- reduced motion makes autoplay inappropriate.

Always clean up timers, animation frames, observers, and media-query listeners.

**Complete when:** normal and reduced-motion runs reach the same semantic end state, keyframe labels match measured choreography, and hidden-tab/offscreen/unmount checks leave no running work.

### 8. Design a mobile topology

Never treat `width: 100%` as responsive design.

At each narrow breakpoint, decide:

- whether a horizontal chain becomes vertical;
- whether branches remain adjacent to their source;
- whether labels move outside shapes;
- whether a wide SVG needs an alternate viewBox or separate mobile geometry;
- whether a figure sheet becomes a labelled horizontal scroller;
- whether the detail panel moves after the figure;
- whether controls become a two-column or one-column grid.

Keep every interactive target at least 44 by 44 CSS pixels. Preserve source and destination context when converting horizontal motion to vertical motion.

**Complete when:** desktop, 390px, and 320px or 200% zoom topologies are specified before coding, with no clipped internal canvas and no illegible SVG labels.

### 9. Make accessibility part of the model

Every figure needs:

- a visible heading;
- a visible explanation;
- a programmatic name;
- a programmatic description;
- a logical reading order;
- keyboard-operable controls;
- visible focus;
- text that communicates the current state;
- status updates through a restrained `aria-live="polite"` region;
- a reduced-motion equivalent.

For SVG:

```tsx
<svg role="img" aria-labelledby={`${titleId} ${descriptionId}`}>
  <title id={titleId}>Literal figure title</title>
  <desc id={descriptionId}>Complete current-state description.</desc>
  <g aria-hidden="true">{/* decorative connectors */}</g>
</svg>
```

For interactive nodes, prefer native `<button type="button">` elements. Use `aria-current="step"` for the active step and `aria-pressed` for toggles. Do not recreate buttons inside SVG unless geometry makes it unavoidable.

A hidden desktop SVG and visible mobile SVG may both exist in the DOM, but only the visible version should be exposed to assistive technology. Prefer CSS `display: none` for the inactive variant, and give each variant unique title, description, marker, mask, and gradient IDs.

Measure rendered contrast: at least 4.5:1 for normal text and 3:1 for large text and essential UI or graphic boundaries where applicable. Test forced-colors mode and preserve visible focus and state without relying on authored color.

**Complete when:** the accessibility tree matches visual order, keyboard operation reaches every state, dynamic descriptions match current values, contrast is measured, and forced-colors plus reduced motion preserve the lesson.

### 10. Namespace SVG internals

Inline SVG IDs share the page namespace. Never ship generic IDs such as `arrow`, `gradient`, or `clip` in reusable components.

```tsx
const markerId = useId().replaceAll(":", "");

<marker id={markerId}>...</marker>
<path markerEnd={`url(#${markerId})`} />
```

Also namespace:

- masks;
- clip paths;
- filters;
- gradients;
- CSS keyframe names when styles are global.

Treat externally sourced SVGs as untrusted input. Inspect scripts, event handlers, `foreignObject`, remote URLs, data URLs, embedded fonts, licenses, and provenance before inlining.

**Complete when:** every inline identifier is instance-scoped and every external influence has a pinned source, license, provenance decision, and explicit record of whether code or assets were redistributed.

### 11. Share framing, not subject geometry

Good shared primitives:

- `DiagramFigure` or `DiagramFrame`;
- `ControlGroup`;
- `ControlButton`;
- `DetailPanel`;
- `MetricStrip`;
- `Glossary`;
- `usePrefersReducedMotion`;
- visibility-aware playback;
- consistent semantic color and typography tokens.

Usually local to each figure:

- node positions;
- edge paths;
- branch geometry;
- domain calculations;
- explanatory copy;
- mobile topology.

Promote a primitive only after at least two real figures need the same behavior.

**Complete when:** every shared primitive has at least two real consumers, and subject-specific geometry remains local.

Start with the split templates:

- [`templates/diagram-primitives.tsx`](templates/diagram-primitives.tsx): server-compatible frame and SVG helpers;
- [`templates/diagram-client.tsx`](templates/diagram-client.tsx): client-only controls and environment hooks;
- [`templates/causal-flow-example.tsx`](templates/causal-flow-example.tsx): one complete typed causal model;
- [`templates/diagram.module.css`](templates/diagram.module.css): container-query and forced-colors starter;
- [`templates/css-modules.d.ts`](templates/css-modules.d.ts): generic TypeScript CSS-module declaration.

## Review Mode

When reviewing an existing diagram, do not silently redesign it. Inspect source and rendered behavior, then report:

1. **Severity:** blocker, high, medium, or polish.
2. **Evidence:** exact file and line plus a runtime observation when behavior is involved.
3. **Impact:** what the reader, keyboard user, assistive-technology user, or maintainer experiences.
4. **Smallest fix:** the minimum change that restores the explanatory contract.
5. **Verification:** the exact state, viewport, input method, or command that proves the fix.

End with one verdict:

- **Block:** an explanatory, functional, responsive, motion, or accessibility requirement is broken.
- **Approve with notes:** the claim remains correct and usable; remaining findings are non-blocking.
- **Approve:** no material findings remain after executed checks.

Do not call source-only inspection a runtime pass. Do not turn personal visual preference into a blocker without tying it to the claim, system, or verified usability.

## Visual language

Use a disciplined hierarchy:

- one display face or strong heading style;
- system sans for explanation and controls;
- monospace for IDs, timings, counters, phases, and code;
- one accent for focus or current action;
- one success color;
- one failure color;
- neutral structure for everything else.

Prefer flat or lightly raised surfaces, thin borders, clear spacing, and semantic contrast. Avoid decorative gradients, glass effects, oversized icons, and a canvas full of identical blue boxes.

Use line weight as grammar:

- neutral solid line: normal dependency or direction;
- accent solid line: active transfer;
- dashed line: retry, conditional branch, or feedback;
- muted line: inactive or contextual path.

Add a legend only when the visual encoding cannot be learned directly from labels and states.

## Acceptance Gates

Do not call the diagram complete until all applicable gates pass.

### Functional

- Every control changes the intended state.
- Back, next, reset, direct selection, and failure branches agree.
- Counters and descriptions update from the same source state.
- Boundary inputs and terminal states behave correctly.
- Timers and observers stop when expected.

### Visual

- Desktop and light/dark themes render correctly.
- At 390 CSS pixels, document width equals viewport width.
- At 320 CSS pixels or 200% zoom, no required text or control disappears.
- Do not treat document width as sufficient when a figure uses `overflow: hidden` or `overflow: clip`; compare critical containers' `scrollWidth`/`clientWidth` and child bounding rectangles to catch silently clipped controls.
- Mobile topology preserves reading order and branch meaning.
- Labels remain legible without zooming.
- Static export crops preserve labels and captions.

### Accessibility

- Keyboard order follows visual and conceptual order.
- Focus is visible.
- Buttons have accessible names and 44×44 targets.
- SVGs have unique labelled descriptions.
- Dynamic status uses polite announcements.
- Color is not the only status signal.
- Reduced motion reaches the same end state without spatial travel.

### Engineering

- Lint passes.
- Type checking passes.
- Production build passes.
- Browser console has no errors.
- No duplicate DOM or SVG IDs exist.
- No document-level horizontal overflow exists.
- External assets have documented license and provenance.
- No copied demo code is shipped without verifying its maintenance status and license.

Use the checklist in `references/verification.md` for an executable review sequence.

## Common Pitfalls

Reject or revise diagrams that:

- animate before the static state is understandable;
- use autoplay without pause and direct controls;
- expose controls that do not change the lesson;
- rely on hover for definitions;
- report random or unseeded educational outcomes;
- shrink a wide desktop SVG until labels become unreadable;
- use a generic component API that fights subject-specific topology;
- encode state only through color;
- put essential prose inside tiny SVG text;
- animate layout dimensions and make the page jump;
- copy visual assets without provenance review;
- use Canvas without a semantic equivalent;
- claim accessibility because an SVG has `role="img"` but omit the current state from its description.

## Linked References

- [`references/research-notes.md`](references/research-notes.md): source observations and what to adapt or avoid.
- [`references/verification.md`](references/verification.md): browser, mobile, motion, and accessibility QA.
- [`references/code-review-pitfalls.md`](references/code-review-pitfalls.md): runtime defects that source-only review often misses.
- [`templates/diagram-contract.md`](templates/diagram-contract.md): pre-build explanatory brief.
- [`templates/diagram-primitives.tsx`](templates/diagram-primitives.tsx): server-compatible React framing and SVG helpers.
- [`templates/diagram-client.tsx`](templates/diagram-client.tsx): client-only controls and environment hooks.
- [`templates/causal-flow-example.tsx`](templates/causal-flow-example.tsx): typed end-to-end causal example.
- [`templates/diagram.module.css`](templates/diagram.module.css): responsive, forced-colors-aware CSS starter.
- [`templates/css-modules.d.ts`](templates/css-modules.d.ts): generic CSS-module declaration.

## Verification Checklist

1. Complete the four-line contract in [`templates/diagram-contract.md`](templates/diagram-contract.md).
2. Run every applicable gate in [`references/verification.md`](references/verification.md).
3. Record commands, viewports, states exercised, issues fixed, provenance decisions, and remaining limitations.
4. For review work, return a severity-ordered report and final verdict.
5. For build work, return the working artifact plus real lint, type, build, browser, mobile, motion, and accessibility evidence.

The task is complete only when every required state is exercised, every modified file is accounted for, and publication or handoff includes a verifiable path or URL.
