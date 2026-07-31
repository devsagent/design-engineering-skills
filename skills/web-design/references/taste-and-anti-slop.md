# Taste and anti-slop

Use this reference when taste is central to the request, when the user asks for a premium or distinctive result, when designing a marketing/editorial/portfolio surface, or when an existing interface feels generic despite being technically competent.

This is not a style preset. Taste is the ability to select, combine, and remove ideas in service of a specific product. The brief always outranks the preferences below.

## The point of view

Prefer interfaces that are:

- specific rather than trend-assembled
- restrained rather than under-designed or over-decorated
- typographically confident rather than dependent on effects
- tactile where interaction benefits from feedback
- editorial in hierarchy, not necessarily in visual style
- technically precise in spacing, geometry, states, and responsiveness
- honest about product capabilities, assets, data, and social proof
- memorable through one or two strong decisions rather than many weak flourishes

The desired reaction is not “this has a lot of design.” It is “this could only belong to this product.”

## Anti-default discipline

Language models and template libraries converge on statistically safe completions. The result can be polished and still feel interchangeable.

Before committing to a direction:

1. Describe the most obvious version of the page.
2. Identify which parts came from the brief and which came from habit.
3. Reject at least the habitual choices that do not serve the product.
4. Preserve familiar conventions where they help comprehension.
5. Spend novelty on the one or two moments that carry identity.

Do not make everything unusual. Generic structure with one meaningful product-specific idea is often stronger than a page of unrelated novelty.

## The specificity brief

Add these fields to the design read when anti-slop quality matters:

- **Product truth:** the real capability, object, behavior, or belief the interface can demonstrate.
- **Emotional target:** what the user should feel: trust, urgency, curiosity, calm, control, delight, or something else.
- **Recognition anchor:** one visual, verbal, or interactive idea that could become recognizable without the logo.
- **Evidence:** real screenshots, data, diagrams, photography, customer proof, or working interaction available to support the claim.
- **Avoid list:** three defaults that would make this product look like its category instead of itself.
- **Novelty budget:** one primary signature move and, at most, one supporting move.

If no product truth or evidence exists yet, design a truthful placeholder state and name what asset is missing. Do not manufacture credibility to fill the composition.

## Direction gate

A direction is ready only when each answer is concrete:

1. Why does this aesthetic fit this audience and task?
2. What existing brand or product signals does it preserve?
3. What is the main visual anchor?
4. What is intentionally quiet?
5. What is the signature move?
6. What common category pattern is being rejected, and why?
7. How does the composition collapse on mobile?
8. How will the direction survive real copy, data, and edge states?

“Modern,” “premium,” “clean,” “bold,” and “minimal” are not directions by themselves. Translate them into observable choices.

## Taste defaults

Use these as bias corrections, not universal laws:

- Begin with hierarchy, type, spacing, and content. Add material effects last.
- Prefer one coherent neutral temperature and one primary accent family.
- Use a restrained radius system with explicit roles instead of making every object a pill or soft card.
- Give the page one lighting model across borders, highlights, shadows, and overlays.
- Let empty space create emphasis, but do not use emptiness to disguise weak content.
- Use cards only when grouping, interaction, or elevation needs a boundary.
- Keep controls and changing values dimensionally stable.
- Make imagery and product evidence do real explanatory work.
- Use motion for hierarchy, continuity, feedback, causality, or storytelling.
- Remove any element that exists only to make the page “feel designed.”

## Slop taxonomy

The patterns below are diagnostic signals. A pattern can be appropriate when the brief justifies it. Habit is not justification.

### Composition slop

Watch for:

- a centered hero containing an eyebrow, giant headline, paragraph, two buttons, trust row, statistics, and decorative status copy
- three equal feature cards used because the content happened to be three items
- automatic bento grids with no relationship between cell shape and content
- long runs of alternating image-left/text-right sections
- the same card row or split-header composition repeated throughout the page
- every section wrapped in its own rounded container
- a large left headline with a small right-side paragraph floating only to fill the grid
- decorative side rails, crosshairs, grid lines, or section numbers that organize nothing
- oversized navigation or hero spacing that pushes the primary action below a normal laptop viewport
- mobile treated as desktop columns stacked in source order without reconsidering priority

Corrections:

- Give the hero one job and one visual anchor.
- Choose section geometry from the content relationship: sequence, comparison, proof, exploration, or action.
- Change layout family when the information pattern changes, not merely to create variety.
- Remove containers until grouping becomes unclear, then add back the minimum boundary.
- Write the narrow-screen composition explicitly for every asymmetric or overlapping section.

### Typography slop

Watch for:

- the same neutral sans used automatically for every product
- a fashionable serif added only to signal “editorial” or “luxury”
- a random italic or second typeface used to emphasize one word in a headline
- oversized display type compensating for a weak message
- uppercase, wide-tracked eyebrow labels above every section
- many nearly identical type sizes without a clear role
- low-contrast small text presented as sophistication
- centered body copy with long line lengths
- display words clipping italics, diacritics, or descenders
- headings that look good only with carefully short placeholder copy

Corrections:

- Choose type from content, audience, language support, and brand voice.
- Prefer emphasis within the same family unless a second family has a defined role.
- Ration eyebrows. If the headline already names the section, remove the label.
- Test the full character set, real punctuation, long words, numeric content, and localization expansion.
- Make hierarchy survive when color, borders, and effects are removed.

### Color and material slop

Watch for:

- purple-blue glows or gradient text used as automatic “AI” styling
- warm cream, brass, clay, and dark brown applied reflexively to every premium consumer brand
- glass panels, blur, grain, or chrome added without a material concept
- multiple accent colors without semantic roles
- warm and cool neutral ramps mixed accidentally
- light and dark sections alternating without narrative purpose
- pure black shadows that conflict with the surface hue
- every object elevated with border, shadow, and glow at once
- source tokens that appear accessible while rendered gradients, alpha, or active fills are not

Corrections:

- Derive the palette from brand, content, imagery, and emotional target.
- Lock neutral temperature, accent family, depth model, and theme behavior.
- Choose one material idea. Do not stack every premium effect.
- Validate computed foreground/background pairs in the rendered state, not just token values.
- Use contrast and spacing to create hierarchy before adding glow or blur.

### Component slop

Watch for:

- one filled button plus one ghost button repeated in every section
- pills for every label, filter, status, and navigation state
- an icon beside every heading whether or not it clarifies meaning
- generic bordered white cards for unrelated content types
- modals used for tasks that could happen inline
- hover motion on non-interactive surfaces
- circular spinners where the layout could preserve its shape with a skeleton
- empty states that are simply blank cards
- success, selected, or active states that shift geometry
- a product interface built entirely around the expected left-sidebar layout without considering the task

Corrections:

- Match component form to behavior and information hierarchy.
- Keep the number of visual control styles small.
- Use native structure and progressive disclosure before decorative containers.
- Design complete state cycles, not only the successful screenshot.
- Apply tactile feedback to actions, not to every surface.

### Imagery slop

Watch for:

- fake dashboards, terminals, browser windows, charts, or task lists assembled from decorative rectangles
- product screenshots that show a fictional capability as if it exists
- generic generated illustrations that could belong to any company
- text-only “minimalism” used because visual direction was never developed
- stock photography with unrelated subject matter or inconsistent art direction
- labels, pills, fake frame numbers, or poetic captions pasted over every image
- logo walls made from plain text names or invented customer logos presented as real
- important text baked into generated imagery
- desktop crops reused on mobile without focal-point decisions

Corrections:

- Prefer real product captures, real data, diagrams, or brand assets.
- If generated imagery is appropriate, create a small coherent reference set with explicit subject, light, lens, palette, and crop direction.
- Label mockups and sample data honestly.
- Use deterministic HTML for meaningful text.
- If an asset does not exist, reserve the correct space and specify exactly what is needed.

### Motion slop

Watch for:

- every section fading upward on scroll with the same timing
- several marquees or perpetual loops on one page
- scroll hijacking, pinned sections, parallax, magnetic buttons, or custom cursors added as proof of craft
- slow entrances delaying routine tasks
- animation that ignores the input source or cannot be interrupted
- layout animation hiding unstable geometry
- motion intensity claimed in the direction but absent in the shipped interface
- automatic motion with no reduced-motion path

Corrections:

- Write one sentence describing what each animation communicates.
- Remove the animation if the sentence only says it looks polished.
- Keep frequent actions immediate and reserve choreography for rare explanatory moments.
- Use one narrative motion device, if any, and quieter feedback elsewhere.
- Test interruption, reversal, keyboard use, touch, document visibility, and reduced motion.

### Copy slop

Watch for:

- vague verbs such as elevate, unlock, unleash, transform, supercharge, revolutionize, and reimagine
- claims such as seamless, powerful, intuitive, next-generation, or best-in-class without evidence
- “not just X, but Y” constructions used for manufactured depth
- rule-of-three slogans assembled for rhythm rather than meaning
- poetic craft labels where a plain section name would be clearer
- fake version strings, timestamps, weather, location, or command-line metadata used as atmosphere
- “quietly trusted by,” “from the field,” “on our desks,” and similar performative microcopy
- invented precise metrics, testimonials, customer names, specifications, awards, or live activity
- multiple labels for the same action: “Get started,” “Try free,” and “Sign up” all competing on one page
- error messages that are cute, apologetic, or vague instead of useful
- every sentence having the same polished rhythm

Corrections:

- Name the object, action, audience, and result concretely.
- Use one label for each action intent across navigation, hero, body, and footer.
- Read every visible string aloud.
- Replace unsupported persuasion with product demonstration.
- Prefer a plain sentence over a clever sentence that does not quite make sense.
- Keep voice consistent, but allow natural variation in sentence length and structure.

### Evidence slop

Watch for:

- fake social proof, logos, users, rankings, or adoption numbers
- precise-looking charts fed by invented data
- testimonials without a real source or explicit mock label
- product promises visualized through non-functional fake controls
- polished case studies with no concrete starting point, intervention, or outcome
- trust badges or security claims unsupported by the product

These are hard failures, not style warnings. Remove them or label them clearly as examples.

## Pattern budgets

Budgets keep a strong device from becoming a template:

- **Signature move:** one primary, one supporting at most.
- **Accent family:** one primary family; semantic colors remain semantic.
- **Hero:** one core idea, one primary action, and only the support needed to understand it.
- **Eyebrows:** occasional categorization, never automatic section furniture.
- **Marquee or perpetual ambient loop:** usually zero, at most one when the content benefits.
- **Major layout family:** avoid using the same family three times in succession.
- **Card treatment:** one system with content-driven variants, not a new card style per section.
- **Display type trick:** one recognizable device is enough.
- **Material effect:** choose the material that supports the concept; do not combine glass, grain, glow, chrome, and mesh by default.

These budgets are defaults. A data-dense product, a long editorial page, or an intentionally repetitive campaign may justify different limits. State the reason.

## The anti-slop workflow

### 1. Inventory truth

Collect real copy, product behavior, imagery, data, brand assets, and edge cases. Mark anything fictional, illustrative, or missing.

### 2. Name the obvious default

Write the version an undirected template would produce. This makes invisible habits visible.

Example:

```text
Centered gradient hero → logo wall → three feature cards → bento grid → testimonials → large CTA.
```

Do not ban the whole sequence automatically. Identify which pieces are unsupported by the brief.

### 3. Choose the recognition anchor

Select one idea rooted in product truth:

- a real interaction shown at useful scale
- an unusual but content-driven grid
- a strong typographic behavior
- an ownable image treatment
- a diagram or data view that teaches the product
- a material metaphor connected to the product
- a distinctive navigation or transition that improves orientation

If the anchor can be swapped into five unrelated products unchanged, it is not specific enough.

### 4. Lock and compose

Set type, palette, spacing, shape, depth, icon, motion, and copy rules. Then compose the page around the recognition anchor rather than filling a standard sequence of sections.

### 5. Build one representative slice

Use real content and include one responsive transition, one state change, and the primary visual language. Render it before scaling the direction.

### 6. Run subtraction

For every badge, card, divider, icon, label, effect, and animation, ask:

- What information or behavior disappears if this is removed?
- Does it support the recognition anchor?
- Is it compensating for weak hierarchy?
- Is it repeating a device already used elsewhere?

Remove elements whose only defense is “it adds polish.”

### 7. Run adversarial audits

Use the tests below against the actual interface.

## Taste tests

### The swap test

Replace the logo and product name mentally. If the page could advertise an unrelated product with no structural changes, the design lacks specificity.

### The squint test

Blur or squint at the page. The major hierarchy and action path should remain obvious. If only decoration survives, rebuild the composition.

### The grayscale test

Remove color. Hierarchy, grouping, and state should remain understandable. Color should reinforce structure, not create it alone.

### The subtraction test

Remove the most decorative element. If the design collapses, it was relying on garnish. If it improves, keep it removed.

### The repetition test

View all sections or screens together. Mark every repeated layout family, card shell, eyebrow, visual effect, and motion pattern. Repetition should communicate system or comparison, not reveal template inertia.

### The truth test

For every image, metric, quote, logo, chart, and claim, identify its source or label it as mock/sample content. Unsupported precision fails.

### The read-aloud test

Read all visible copy in order. Remove vague claims, forced cleverness, duplicated action labels, unexplained metaphors, and sentence fragments that exist only for rhythm.

### The first-frame test

At a normal laptop and a narrow phone, the first viewport should establish identity, value, and a next action without overcrowding or hiding the rest of the page behind excessive hero height.

### The edge-state test

Replace ideal content with long names, missing media, zero data, slow loading, errors, localization expansion, keyboard focus, and reduced motion. Taste that survives only the perfect screenshot is not production quality.

### The memory test

After looking away, name the one thing that made the interface distinct. If the answer is only “dark,” “minimal,” “gradient,” “bento,” or “smooth,” the concept is too generic.

## Context overrides

Anti-slop work must not punish useful conventions.

### Product and operational UI

Predictability, density, and speed often matter more than visual variance. A sidebar, table, cards, neutral sans, or familiar filter pattern may be correct. Distinction should come from information architecture, excellent states, interaction quality, and a coherent system rather than forced asymmetry.

### Public-sector, regulated, health, and financial surfaces

Trust, clarity, accessibility, and established design systems override novelty. Do not reject a conventional pattern merely because it is common.

### Editorial surfaces

Typography and rhythm may be the primary visual system. Do not force product screenshots, cards, or interactive demos into content that benefits from quiet reading.

### Campaign and experimental surfaces

Higher variance and narrative motion may fit, but orientation, performance, accessibility, and a clear action still matter. Novelty needs a compositional thesis.

### Existing brands

A redesign begins with preservation. A common pattern that is already recognizable brand equity is not slop. Evolve it deliberately instead of erasing it for novelty.

## Audit output

When performing a taste or anti-slop review, separate evidence from preference:

| ID | Signal | Evidence | Why it feels generic or mismatched | Product-specific correction | Gate |
| --- | --- | --- | --- | --- | --- |
| TASTE-001 | Repeated three-card rows | observed | Different content relationships use the same template | Turn proof into a real product demonstration and group supporting details separately | block / note |

Use **block** only for:

- fabricated or misleading evidence
- severe mismatch with audience, task, or brand
- inaccessible contrast, interaction, or motion
- broken responsive composition
- inconsistent system decisions that materially harm comprehension
- missing critical states or non-functional primary paths

Use **note** for a recognizable design cliché that is coherent and usable but could be made more specific.

## Taste preflight

Before shipping, answer yes to every applicable gate:

- [ ] The direction is derived from product, audience, task, brand, and constraints.
- [ ] Product truth and evidence are visible in the composition.
- [ ] The design has a recognition anchor that cannot be swapped unchanged into an unrelated product.
- [ ] The novelty budget is explicit and restrained.
- [ ] Type, palette, spacing, shape, depth, icons, motion, and copy follow one system.
- [ ] The hero communicates one idea without becoming a badge, statistic, trust, and CTA pile.
- [ ] Section geometry changes when the content relationship changes.
- [ ] Cards, pills, eyebrows, gradients, glass, and glows are used for a reason rather than as default furniture.
- [ ] Real or truthfully labeled imagery, data, proof, and product UI replace fabricated atmosphere.
- [ ] Visible copy is concrete, consistent, and natural when read aloud.
- [ ] Every animation has a stated job and an accessible fallback.
- [ ] Mobile is recomposed intentionally, with no accidental overflow or hidden primary action.
- [ ] Loading, empty, error, long-content, keyboard, touch, theme, and reduced-motion states preserve the design.
- [ ] The swap, squint, grayscale, subtraction, repetition, truth, first-frame, edge-state, and memory tests pass.
- [ ] The rendered result was inspected after the final relevant edit.

If a gate fails, revise the underlying direction or system. Do not add more decoration to hide the problem.
