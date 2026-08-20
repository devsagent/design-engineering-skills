# Verification checklist

Run the checks that match the project. Record exact commands, viewport sizes, and real outputs. Do not report a gate as passed from source inspection alone.

## 1. Static checks

Inspect the project manifest, lockfile, and documented scripts first. Then use the repository's own package manager and canonical commands, for example:

```bash
<package-manager> run lint
<package-manager> run typecheck
<package-manager> run build
```

If no type-check script exists, use the locally installed compiler through the project's package manager. Do not use a command that can fetch a replacement compiler or package from the network without approval. Explain every compatibility flag.

Also run:

```bash
git diff --check
```

Inspect the diff for:

- accidental generated files;
- external assets without provenance;
- global CSS leakage;
- generic SVG IDs;
- copied code;
- unrelated changes.

## 2. Desktop browser

Test the built or development route at its normal desktop width.

Verify:

- the route loads with no JavaScript error;
- visible heading order is logical;
- each figure has a visible question or claim;
- controls sit next to the state they affect;
- connectors meet their source and destination;
- labels are not clipped;
- details do not overlap the figure;
- light and dark themes preserve semantic colors;
- normal text measures at least 4.5:1 contrast, and large text plus essential UI or graphic boundaries measure at least 3:1 where applicable;
- forced-colors or high-contrast mode preserves focus, current state, success, and failure;
- no document-level horizontal overflow exists.

Useful console probe:

```js
(() => {
  const root = document.documentElement;
  const ids = [...document.querySelectorAll("[id]")].map((node) => node.id);
  const duplicates = ids.filter((id, index) => ids.indexOf(id) !== index);
  const controls = [...document.querySelectorAll("button, input, select, a[href]")];
  const smallTargets = controls
    .map((element) => {
      const rect = element.getBoundingClientRect();
      return {
        name: element.getAttribute("aria-label") || element.textContent?.trim(),
        width: Math.round(rect.width),
        height: Math.round(rect.height),
      };
    })
    .filter(({ width, height }) => width < 44 || height < 44);

  return {
    viewportWidth: root.clientWidth,
    documentWidth: root.scrollWidth,
    overflow: root.scrollWidth > root.clientWidth,
    duplicateIds: [...new Set(duplicates)],
    smallTargets,
  };
})();
```

Treat inline text links according to WCAG target-spacing rules; do not blindly force every prose link to 44×44.

## 3. Interaction matrix

For every figure, write and execute a small matrix.

### Flow explorer

- initial node and description agree;
- Next advances geometry, detail, and status together;
- Previous reverses the state;
- direct node selection works;
- Reset returns to the documented default;
- Play stops at the terminal state;
- Pause stops advancement;
- success and failure branches end on the correct node;
- changing a branch at the terminal state updates the outcome coherently;
- disabled controls are correct at boundaries.

### Parameter explainer

- minimum input;
- maximum input;
- balanced or equilibrium input;
- first overloaded input;
- full capacity;
- overflow;
- glossary selection;
- SVG description and visible metrics update from the same values.

Check expected arithmetic independently when the model matters.

### Motion bench

- replay from idle;
- replay after completion;
- each duration;
- each easing;
- completion status after the documented duration;
- reduced-motion preview;
- system reduced-motion preference;
- no spatial travel in reduced mode;
- identical semantic end state in both modes.

## 4. Keyboard

Using only the keyboard:

1. Tab through the page.
2. Confirm visual focus on every control.
3. Confirm order matches reading order.
4. Activate buttons with Space and Enter.
5. Change range inputs with arrow, Home, and End keys.
6. Confirm disabled controls are skipped or announced as disabled.
7. Confirm no keyboard trap.
8. Confirm state changes do not move focus unexpectedly.

Do not add custom arrow-key behavior to native controls unless the interaction pattern requires it.

## 5. Accessibility tree

Inspect the browser accessibility tree.

Expected shape:

- one page heading;
- one region or figure per diagram;
- visible diagram title used as the accessible name;
- visible explanation plus current status used as the description;
- native buttons and sliders with literal names;
- definition list for a glossary;
- `role="img"` SVG with title and full description;
- decorative connectors hidden;
- current step exposed with `aria-current="step"`;
- toggles exposed with `aria-pressed`;
- status announced politely.

Inspect descriptions after changing state. A static SVG description that contradicts current values is a failure.

## 6. Mobile and reflow

Test at:

- 390×844 CSS pixels;
- 320 CSS pixels when practical;
- 200% browser zoom on a 1280px-wide desktop viewport.

Verify:

- `document.documentElement.scrollWidth === document.documentElement.clientWidth`;
- headings wrap without clipping;
- node order remains conceptual;
- branches remain attached to their source;
- horizontal transfers become vertical when needed;
- internal SVG labels remain legible;
- the detail panel follows the figure;
- controls wrap into usable rows;
- every non-inline control is at least 44×44 CSS pixels;
- horizontal figure sheets have an obvious next item and labelled scrolling context;
- anchor links land below sticky navigation.

A desktop SVG scaled to 45% is not a mobile implementation if 12px labels become 5px labels. Use alternate geometry or a deliberate scroller.

## 7. Reduced motion

Enable the operating-system or browser `prefers-reduced-motion: reduce` setting.

Verify:

- media query matches;
- autonomous animations stop or collapse to an effectively zero duration;
- the current and terminal states remain visible;
- transitions do not rely on travel to communicate meaning;
- autoplay does not restart unexpectedly;
- pause and replay controls remain coherent;
- animated SVG and CSS keyframes both honor the preference.

Do not remove the result when removing the travel.

## 8. Visibility and cleanup

While playback runs:

- move the figure offscreen;
- switch tabs;
- return to the page;
- unmount or navigate away.

Verify timers and animation frames stop, observers disconnect, and playback resumes only if that is the documented behavior.

## 9. Visual review

Take screenshots of:

- desktop default;
- desktop failure or overloaded state;
- light theme;
- mobile default;
- mobile alternate topology;
- reduced-motion terminal state;
- figure sheet or export crop.

Review at 100% scale. Check:

- hierarchy before decoration;
- line and node alignment;
- semantic color;
- label density;
- crop boundaries;
- control proximity;
- uneven spacing;
- tiny text;
- decorative motion that competes with the claim.

## 10. Completion record

Report:

- commands run and exit status;
- browser route;
- viewports tested;
- states exercised;
- issues found and fixes applied;
- remaining limitations;
- provenance and license notes;
- commit or review URL when published.

Never replace missing execution with plausible output.
