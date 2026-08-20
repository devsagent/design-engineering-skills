# Diagram code-review pitfalls and runtime probes

Use this during source reviews of React/SVG diagram systems. These checks catch defects that lint, type checking, builds, and ordinary interaction tests often miss.

## Geometry and motion

- Treat a curved connector and its arrowhead as one geometric object. Prefer `marker-end` with `orient="auto"` over a separately positioned chevron. Verify the curve endpoint, the final tangent, the marker reference, and draw order. A marker can be mathematically attached but visually hidden under its destination node; stop the path just before the node or layer it deliberately.
- For a curve that should enter a node at a precise side, align the final Bézier control point with the endpoint and target center. Measure the rendered tangent with `getPointAtLength(totalLength - 1)` and `getPointAtLength(totalLength)` rather than judging source coordinates alone.
- CSS transform percentages are relative to the transformed element, not its parent. A token with `width: 0.84rem` and `translateX(calc(100% - 0.84rem))` moves approximately zero. Measure the token and track rectangles midway through animation.
- For parent-relative travel, use a parent-width carrier, `offset-distance`, or a bounded `left` animation when the surface is small and profiling permits it.
- Test Replay followed immediately by Reset. An uncancelled `requestAnimationFrame` can restart playback after reset.
- Changing duration while a run is active can restart a completion timer without restarting the visual animation. Either restart the run transactionally or disable tuning during playback.
- Prefer one phase state such as `idle | running | complete` over independent booleans that admit stale combinations.

## Responsive overflow

Document-level overflow checks are insufficient when an ancestor uses `overflow: hidden` or `overflow: clip`; clipped controls can coexist with `documentElement.scrollWidth === clientWidth`.

At 320px, inspect each critical container:

```js
const rect = element.getBoundingClientRect();
({
  left: rect.left,
  right: rect.right,
  clientWidth: element.clientWidth,
  scrollWidth: element.scrollWidth,
  viewport: document.documentElement.clientWidth,
});
```

Flag required content when:

- a child rect crosses the clipping ancestor's rect;
- `scrollWidth > clientWidth` on a non-scrollable clipped container;
- a range control's fixed/vw-sized input forces its output outside the figure;
- mobile CSS hides labels that are part of the figure's stated lesson.

For mobile range layouts, commonly needed safeguards are `min-width: 0`, `flex: 1` on the input, and making the range row span all mobile control-grid columns.

## Topology correctness

- Derive edge completion separately from node completion. In a failure branch, the source node may have run while its success edge must remain inactive.
- Exercise success and failure terminal states and inspect every connector, muted node, detail label, and status together.
- A branch outcome should not inherit a misleading main-path phase label such as “phase 5 of 5” when it replaces phase five.
- Reset should restore the documented default. If branch persistence is intentional, name the action narrowly, such as “Reset position.”

## Touch, hover, and selected state

- Pressed feedback, hover, focus, and selected state are different. A tap should not show a dull hover color before the selected color appears.
- Gate hover rules behind `@media (hover: hover) and (pointer: fine)`. Mobile Safari can preserve hover after a tap even when desktop emulation looks correct.
- On coarse pointers, prefer immediate semantic border/background/text changes and a short transform-only press transition. Animating selected colors from neutral can make the state look delayed or require several taps to understand.
- Set `touch-action: manipulation` on native diagram controls and make tap-highlight policy explicit. Verify computed `transition-property`, `aria-pressed`, and `data-active` under real or CDP-emulated coarse-pointer media.

## Landmarks and ARIA

- Inspect enclosing layouts before adding `<main>`; route components frequently render inside a site-level main landmark. Confirm the runtime accessibility tree has exactly one main.
- Separate visual `active` styling from `aria-pressed`. Replay and other momentary commands are not pressed toggles.
- Keep `<ol>` children valid: overlays and playheads belong in a sibling wrapper or an `aria-hidden` `<li>`.
- Native `<output>` is commonly exposed as a status. If the figure caption is also live, range changes may create competing announcements. Put units in `aria-valuetext` and choose deliberate live-region ownership.

## SVG variants and IDs

- `display: none` is appropriate for the inactive desktop/mobile SVG variant; verify computed display at both breakpoints.
- Give each variant unique title, description, marker, mask, filter, clip-path, and gradient IDs.
- Check both current duplicate IDs and latent reusable-component collisions. Hard-coded IDs may be collision-free with one instance but fail when a component is rendered twice.

## Compact runtime probe set

Record observed values rather than relying only on screenshots:

1. Count `main` landmarks and duplicate IDs.
2. Check computed display for desktop and mobile SVG variants.
3. Sample moving-element and track rectangles midway through animation.
4. Trigger Replay then Reset inside one frame and inspect resulting state.
5. At 320px, compare clipped container `clientWidth`, `scrollWidth`, and child bounds.
6. Activate the failure terminal state and inspect connector styles, not just node styles.
