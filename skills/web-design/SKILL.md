---
name: web-design
description: "Use when designing, redesigning, critiquing, or polishing a web interface. Establishes a brief-led visual direction, coherent design system, responsive behavior, complete interaction states, accessible motion, and evidence-based craft review without defaulting to generic templates."
version: 1.0.0
author: devsagent
license: MIT
metadata:
  tags: [web-design, ui, ux, design-systems, responsive-design, accessibility, motion]
  related_skills: [frontend-development]
---

# Web Design

## Overview

Design interfaces that feel intentional, specific, coherent, and usable. Start from the product and audience rather than a default aesthetic. Build a small visual language, apply it consistently, and verify the interface across content, states, input methods, themes, and viewport sizes.

The goal is not maximal novelty. The goal is an interface whose hierarchy is immediately legible, whose personality fits its purpose, and whose details quietly reinforce trust.

## When to Use

Use this skill for:

- New product surfaces, landing pages, applications, dashboards, portfolios, commerce, documentation, and editorial experiences.
- Redesigning or polishing an existing interface.
- Defining visual direction, tokens, layout, component behavior, responsive rules, or motion.
- Reviewing screenshots, prototypes, design files, or frontend code for visual and interaction quality.
- Turning an underspecified brief into a concrete design system and execution plan.

Do not use it alone for backend implementation, infrastructure, or a purely functional bug with no interface implications. Pair it with `frontend-development` when code must be shipped.

## Core Operating Principles

1. **Brief before aesthetic.** Product purpose, audience, task, content, and constraints choose the design direction.
2. **Hierarchy before decoration.** Users should know what matters before they notice styling.
3. **System before component.** Shared decisions for type, spacing, color, shape, and motion prevent local improvisation.
4. **Specific before fashionable.** References inform the work; they do not replace a product-specific idea.
5. **States before screenshots.** An interface is a state machine, not one ideal frame.
6. **Responsive by composition.** Mobile is a designed arrangement, not a squeezed desktop.
7. **Motion by causality.** Animate to explain, connect, acknowledge, or preserve context—not to decorate routine actions.
8. **Accessibility by construction.** Contrast, semantics, focus, input equivalence, and reduced motion are design constraints.
9. **Evidence before completion.** Inspect the rendered interface. A code diff or build result cannot prove visual quality.

## Workflow

### 1. Write the design read

Before proposing a layout or visual style, state:

- **Surface:** what kind of interface is this?
- **Audience:** who uses it, and what do they already understand?
- **Primary task:** what must they notice, trust, decide, or complete?
- **Content reality:** what real copy, data, media, and edge cases must fit?
- **Brand signals:** what identity, references, or existing patterns should be preserved?
- **Constraints:** accessibility, performance, device, framework, localization, SEO, legal, or conversion requirements.
- **Direction:** one sentence that describes the intended visual language and why it fits.

If the brief is thin, make the smallest reversible assumptions and label them. Do not hide ambiguity behind a polished generic mockup.

### 2. Choose three design dials

Set these explicitly for the surface:

- **Visual variance:** systematic and predictable ↔ expressive and asymmetric.
- **Information density:** spacious and focused ↔ compact and operational.
- **Motion intensity:** immediate state feedback ↔ occasional narrative choreography.

The dials are contextual, not quality scores. A dense admin tool can be excellent; a sparse campaign can be excellent. Mismatch is the failure.

### 3. Lock the system

Choose once, then document exceptions:

- **Palette lock:** one neutral temperature, one primary accent family, semantic colors reserved for meaning.
- **Type lock:** display, body, UI, and mono roles with explicit sizes, weights, line heights, and tracking.
- **Spacing lock:** a small base rhythm and named section/component intervals.
- **Shape lock:** a restrained radius scale with roles for controls, cards, media, and overlays.
- **Depth lock:** a consistent border, shadow, and material model.
- **Icon lock:** one icon family, stroke weight, optical size, and filled/outlined convention.
- **Motion lock:** shared duration, easing, spring, and reduced-motion rules.
- **Copy lock:** a consistent voice and capitalization register.

A surface should not feel like several templates stitched together.

### 4. Design the composition

Establish the reading and action order before detailed components:

1. What is the first visual anchor?
2. What supporting evidence follows?
3. What is the primary action?
4. What can remain quiet or progressively disclosed?
5. What changes when the viewport narrows?

Use asymmetry only when it improves emphasis or rhythm. Use repetition only when it improves comparison or scanning. Vary section composition intentionally; avoid repeating the same card row throughout a page.

### 5. Define the state matrix

For every interactive or data-backed surface, design applicable states:

- default
- hover on capable pointers
- active/pressed
- keyboard focus
- selected/current
- disabled or unavailable
- loading or pending
- empty or first-use
- error and retry
- success or completion
- validation feedback
- offline or stale data
- permission denied
- long content, missing media, and localization expansion

Keep control dimensions stable across state changes. Do not signal selection by changing font weight, padding, or border width if it causes layout movement.

### 6. Specify responsive behavior

For each multi-column, overlapping, sticky, or wide composition, define:

- What stacks, reorders, collapses, scrolls, or disappears?
- Which element remains primary?
- What becomes a disclosure or menu?
- What keeps a minimum readable/tappable size?
- What may intentionally overflow inside its own region?
- What must never cause document-level horizontal overflow?

Check narrow mobile, wide mobile, tablet, both sides of each breakpoint, normal desktop, and a wide viewport. Content and geometry—not device labels—should determine breakpoints.

### 7. Build the smallest representative slice

Before expanding the entire surface, complete one slice containing:

- the intended type hierarchy
- a primary action
- a representative content component
- one responsive transition
- one interactive state
- real or truthfully labeled content

Render it. If the direction does not hold up, adjust the system before multiplying weak decisions.

### 8. Review and refine

Audit the actual result in this order:

1. hierarchy and comprehension
2. layout and responsive behavior
3. typography and content fit
4. color and contrast
5. interaction states and accessibility
6. motion and continuity
7. imagery, surfaces, and micro-details
8. consistency and unnecessary elements

Removing one weak idea is often more valuable than adding three polish effects.

## Visual System Guidance

### Typography

- Choose type for the product's voice and content, not because it is currently popular.
- Use a deliberate scale; avoid many nearly identical sizes.
- Tighten tracking carefully for large display text. Preserve readability for small text.
- Give body copy enough line height and constrain long prose to a comfortable measure, commonly around 45–75 characters depending on type and context.
- Use `text-wrap: balance` for short headings and `text-wrap: pretty` for prose when supported.
- Use tabular figures for metrics, timers, prices, dates, and values that change.
- Test real punctuation, long words, numeric data, mixed case, and localization expansion.
- Avoid using low contrast, uppercase, and tight tracking together for important labels.

Hierarchy should remain understandable if color and decoration are removed.

### Color

- Prefer perceptual color thinking such as OKLCH when building ramps or themes.
- Use one coherent neutral family; accidental mixing of warm and cool grays creates visual noise.
- Reserve chromatic emphasis for actions, status, selection, or meaningful identity.
- Do not use gradients as a substitute for a design idea.
- Validate the rendered foreground against the actual rendered background, including transparency, gradients, overlays, and active states.
- Meet at least 4.5:1 for normal text and 3:1 for large text and essential non-text boundaries unless the product requires a stricter target.
- Never communicate status by color alone.

For themed interfaces, audit every relevant combination of theme, accent variant, and interactive state. Source tokens do not prove runtime contrast.

### Spacing and layout

- Use a spacing rhythm rather than isolated pixel guesses.
- Let proximity express relationships before adding borders or boxes.
- Give page edges intentional gutters at every viewport.
- Use `min-width: 0` on grid/flex children that must shrink.
- Bound prose, media, tables, and code according to their content needs instead of forcing one universal width.
- Align repeated titles, controls, and actions optically as well as mathematically.
- Allow intentional whitespace, but make sure it improves focus rather than hiding missing content.

### Shape and surfaces

- Use cards only when grouping, interaction, or elevation needs a boundary.
- Avoid wrapping every section in a rounded rectangle.
- Keep nested corners concentric: the outer radius should equal the inner radius plus the intervening padding.
- Establish one lighting model. Borders, inner rings, shadows, and highlights should imply compatible materials.
- Bound screenshots and media with a quiet outline or surface treatment so they do not feel pasted onto the page.
- Treat glass, blur, grain, and glow as optional material cues, not default premium effects.

### Iconography

- Use symbols with clear meaning; avoid decorative icons beside every heading.
- Keep one family and weight across the interface.
- Give icon-only controls an accessible name and a generous hit target.
- Optically adjust arrows, play marks, and asymmetric glyphs rather than relying only on geometric centering.
- Do not use an icon when a short text label is clearer.

### Imagery and generated assets

- Prefer product truth: real screenshots, diagrams, data, photography, or illustrations that support the message.
- Do not fabricate product UI, testimonials, logos, metrics, or evidence for atmosphere.
- When generated imagery is used, establish a coherent art direction and inspect artifacts, legibility, crops, and responsive behavior.
- Keep important text in deterministic HTML whenever accuracy and accessibility matter.
- Define focal points and crops for mobile rather than blindly using `object-fit: cover`.

### Copy

- Use concrete language tied to the user's task.
- Prefer sentence case and active voice.
- Remove empty intensifiers, vague superlatives, and startup clichés.
- Make labels describe the action or destination.
- Error messages should say what happened and what the user can do next.
- Never invent precise numbers, customer quotes, or social proof.

## Interaction and Motion

### Decide whether to animate

For every proposed animation, answer:

- What purpose does it serve: feedback, continuity, hierarchy, causality, or explanation?
- How often will the user trigger it?
- Was it initiated by pointer, touch, keyboard, or the system?
- Must it be interruptible or reversible?
- What happens under reduced motion?

High-frequency and keyboard-triggered actions should usually be instant or nearly instant. Rare explanatory moments may earn more choreography.

### Timing and easing

Use these as starting ranges, then verify in context:

| Interaction | Typical range |
| --- | --- |
| Press feedback | 100–160ms |
| Tooltip or small popover | 125–200ms |
| Select, menu, disclosure | 150–250ms |
| Modal, sheet, drawer | 200–500ms |
| Explanatory sequence | As long as comprehension requires |

- Entering UI usually benefits from responsive deceleration.
- Movement already on screen often benefits from acceleration and deceleration.
- Constant motion uses linear timing.
- Avoid slow-starting motion when the system should acknowledge input immediately.
- Make exits no more theatrical than entrances; response should feel prompt.

### Physical continuity

- Trigger-anchored surfaces should emerge from their trigger; centered dialogs are a common exception.
- Avoid entrances that scale from zero unless disappearance from a point is the actual concept.
- Direct manipulation should preserve the grab offset, pointer identity, live position, and release velocity.
- Gesture-driven motion should be interruptible and retarget from the visible state.
- Use soft resistance at boundaries when it clarifies limits.
- Never block input while animation finishes.

### Performance and motion accessibility

- Prefer compositor-friendly transforms and opacity, but profile the actual surface instead of treating property names as proof.
- Avoid broad `transition: all`, unbounded `will-change`, large animated blurs, and frame-by-frame parent state churn.
- Gate hover behavior with `(hover: hover) and (pointer: fine)`.
- Under `prefers-reduced-motion`, remove large spatial travel, parallax, and decorative loops while preserving understandable state feedback.
- Pause ambient animation when offscreen or when the document is hidden.

## Component Heuristics

### Buttons and controls

- Use a clear action hierarchy; not every action deserves a filled button.
- Provide hover, focus, active, disabled, pending, and success behavior where applicable.
- Aim for a 44×44px hit area when practical and avoid overlapping targets.
- Use subtle press feedback and keep the label/icon geometry stable.
- A disabled control should explain its unavailable state when the reason is not obvious.

### Navigation

- Make the current location clear without layout shift.
- Keep labels stable across active and inactive states.
- Preserve familiar browser behavior for genuine links.
- Avoid hiding primary navigation behind novelty on large screens.
- Mobile navigation must manage focus, Escape, scroll locking, and return focus correctly.

### Forms

- Use persistent labels; placeholders are examples, not labels.
- Put validation near the field and summarize form-level failures when useful.
- Preserve user input after recoverable errors.
- Show pending state without allowing accidental duplicate submission.
- Use appropriate input types, autocomplete attributes, help text, and error associations.

### Data and dashboards

- Keep changing values dimensionally stable.
- Put the most important interpretation near the visualization.
- Do not rely on hover-only tooltips; provide touch, keyboard, and persistent selected-state access.
- Distinguish empty data, loading data, stale data, and failed data.
- Preserve readable point spacing rather than crushing long histories into one viewport.

### Overlays

- Use dialogs for tasks that temporarily own focus; use non-modal panels for parallel context.
- Set initial focus intentionally, trap it only when appropriate, support Escape, and return focus to the trigger.
- Match transform origin and motion to the source of the interaction.
- Ensure background dimming, blur, and depth describe one coherent layer.

## Anti-Template Audit

Treat these as warning signs, not automatic bans:

- A hero overloaded with badges, statistics, trust logos, two buttons, and decorative microcopy.
- A page built mostly from repeated three-card rows or alternating text/image bands.
- Gradient blobs, glass panels, and abstract meshes with no product-specific purpose.
- Every item placed in a bordered rounded card.
- Small uppercase mono labels above every heading.
- Fake dashboards, terminal windows, charts, or browser chrome used as decoration.
- Multiple accent colors with no semantic role.
- Generic illustrations that could be swapped between unrelated products.
- Motion on every scroll event or hover target.
- Copy built from claims such as “revolutionary,” “seamless,” or “next generation.”
- Perfect desktop screenshots with no loading, error, focus, keyboard, or mobile behavior.

For each warning sign, ask: does this improve comprehension, identity, trust, or task completion? If not, remove or replace it.

## Redesign Safety

When improving an existing product:

1. Inventory brand tokens, information architecture, navigation labels, core workflows, signature interactions, accessibility wins, and analytics/SEO-sensitive identifiers.
2. Capture representative screenshots and current behavior before editing.
3. Rank problems by user impact and implementation risk.
4. Modernize in a safe order: hierarchy and type, spacing, color calibration, states, motion, then major recomposition.
5. Preserve functionality and identity unless the brief explicitly changes them.
6. Compare before and after at the same content and viewport sizes.

Do not silently change URLs, forms, legal copy, primary labels, brand marks, data meaning, or conversion paths during a visual redesign.

## Review Format

When reviewing an interface, report only verified or clearly labeled inferred findings. Use:

| ID | Area | Evidence | Problem | Direction | Verification |
| --- | --- | --- | --- | --- | --- |
| DESIGN-001 | Hierarchy | observed | Primary and secondary actions have equal visual weight | Reduce the secondary action and strengthen the content/action order | Recheck first-click comprehension at mobile and desktop widths |

Then provide an explicit verdict:

- **Block:** a verified issue materially harms comprehension, accessibility, task completion, or responsive usability.
- **Approve with notes:** no blocker, but meaningful polish or low-risk improvements remain.
- **Approve:** the intended system, states, accessibility, and responsive behavior hold up in the rendered interface.

Preference alone is not a blocker. Explain why the rule applies to this product and state whether evidence was observed, measured, or inferred.

## Verification Checklist

### Direction

- [ ] The design read identifies surface, audience, task, content, constraints, and direction.
- [ ] The design dials match the product rather than a default aesthetic.
- [ ] System locks are explicit and exceptions are intentional.
- [ ] The interface has one clear visual and action hierarchy.

### System

- [ ] Type roles, line lengths, wrapping, and numeric alignment are intentional.
- [ ] Palette and themes use coherent neutrals and semantic accents.
- [ ] Rendered contrast passes in every relevant theme and state.
- [ ] Spacing, radii, depth, iconography, and copy form one language.
- [ ] Imagery and evidence are real or truthfully labeled.

### Interaction

- [ ] Every relevant state is designed.
- [ ] Keyboard focus is visible and logical.
- [ ] Touch targets are usable and hover is not required.
- [ ] Motion has a purpose, remains interruptible where needed, and supports reduced motion.
- [ ] Overlays, forms, navigation, and data views have complete behavior.

### Responsive QA

- [ ] Mobile is composed intentionally, not merely stacked.
- [ ] Breakpoints are checked on both sides.
- [ ] Long content, missing media, and localization do not break layout.
- [ ] No unintended document-level horizontal overflow exists.
- [ ] Sticky, fixed, overlapping, and wide elements remain usable.

### Completion

- [ ] The real interface was inspected at representative mobile, tablet, and desktop widths.
- [ ] Loading, empty, error, and success states were exercised where applicable.
- [ ] Browser console and interaction paths were checked.
- [ ] Remaining limitations are stated precisely.
