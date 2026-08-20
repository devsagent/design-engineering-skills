# Diagram contract

Complete this before implementation.

## Reader and placement

**Audience:**

**Page or article section:**

**What the reader knows before this figure:**

**What the prose immediately before the figure says:**

## Explanatory contract

**Question:** What should the reader understand?

**Variable:** What can the reader change or inspect?

**Observable:** What visibly proves the relationship?

**Implication:** Why does the change matter?

## Pattern

Select one primary archetype:

- [ ] Static figure
- [ ] Selectable concept map
- [ ] Flow explorer
- [ ] Parameter explainer
- [ ] Comparison panel
- [ ] Animation sandbox
- [ ] Figure sheet

Why this is the smallest adequate pattern:

## Static truth

Describe the default screenshot in literal terms:

**Nodes or entities:**

**Edges or relationships:**

**Direction:**

**Initial state:**

**Terminal or comparison state:**

**Caption:**

**Long description:**

## State model

List named states:

| State | Visible geometry | Detail or status | Available actions |
|---|---|---|---|
| | | | |

List inputs and bounds:

| Input | Type | Minimum | Default | Maximum | Unit |
|---|---|---:|---:|---:|---|
| | | | | | |

List derived values and formulas:

| Output | Formula or rule | Display location |
|---|---|---|
| | | |

## Controls

- [ ] Back
- [ ] Next
- [ ] Play/Pause
- [ ] Reset
- [ ] Direct selection
- [ ] Failure toggle
- [ ] Parameter input
- [ ] Glossary selection
- [ ] Replay
- [ ] Duration
- [ ] Easing
- [ ] Reduced-motion preview

Remove every checked control that does not alter the lesson.

## Visual grammar

**Focus/current color:**

**Success color:**

**Failure color:**

**Neutral structure:**

**Solid line means:**

**Dashed line means:**

**Monospace is used for:**

**Legend required? Why?**

## Motion contract

For each transition:

| Transition | What moves | Why motion helps | Duration | Easing | Reduced-motion equivalent |
|---|---|---|---:|---|---|
| | | | | | |

Autoplay policy:

Offscreen policy:

Hidden-tab policy:

## Responsive topology

| Width | Node layout | Edge direction | Label placement | Controls | Details |
|---|---|---|---|---|---|
| Desktop | | | | | |
| Tablet | | | | | |
| 390px | | | | | |
| 320px / 200% zoom | | | | | |

If using SVG, decide whether mobile uses:

- [ ] same viewBox;
- [ ] alternate viewBox;
- [ ] separate geometry;
- [ ] labelled horizontal scroller.

## Accessibility contract

**Visible title:**

**Programmatic name:**

**Current-state description:**

**Status announcement:**

**Keyboard order:**

**Active-state semantics:**

**Toggle semantics:**

**Decorative content hidden from assistive technology:**

**Color-independent cues:**

## Shared versus local

**Existing primitives to reuse:**

**New primitive justified by at least two figures:**

**Geometry that stays local:**

**External assets and provenance:**

## Verification cases

List the exact states that must be exercised:

1.
2.
3.
4.
5.

Required screenshots:

- [ ] Desktop default
- [ ] Desktop alternate or failure
- [ ] Light theme
- [ ] 390px default
- [ ] 390px alternate topology
- [ ] Reduced-motion terminal state
- [ ] Export crop or figure sheet
