---
name: dotted-painterly-cover-art
description: "Use when creating or replacing editorial covers, blog thumbnails, or social preview images in a dotted ASCII-like painterly style. Defines the visual grammar, concept selection, native-raster workflow, prompt structure, strict text and motif exclusions, crop-aware review, and publication verification needed for distinctive images that remain legible at card size."
version: 1.0.0
author: devsagent
license: MIT
metadata:
  tags: [cover-art, image-generation, thumbnails, art-direction, dithering, stippling, editorial-design, visual-qa]
  related_skills: [web-design]
---

# Dotted Painterly Cover Art

## Overview

Create editorial cover art that combines painterly scenic massing with fine square-cell stippling, ordered dithering, pixel clusters, and posterized tonal bands. The result should feel like a classical oil-painted or travel-poster scene translated through late-1980s or early-1990s computer graphics and printmaking.

This is not ordinary pixel art, a photograph with a halftone filter, or literal ASCII art. **ASCII-like describes the repeated mark language, not readable characters.** The cells must construct volume, light, depth, and material. A uniform dot overlay on flat vector shapes does not satisfy the direction.

The goal is a memorable physical image that communicates the subject at full size and at thumbnail size. Texture, palette, and atmosphere support the concept; they do not replace it.

## When to Use

Use this skill for:

- Blog covers, article thumbnails, editorial hero images, and social preview cards.
- A user asking for dotted, ASCII-like, dithered, pixel-mosaic, stippled, vintage-computer, or painterly poster imagery.
- Replacing a cover while preserving its overall vibe but removing a rejected central motif.
- Turning an abstract topic into one clear scenic or physical metaphor.
- Creating a textless generated background that will receive deterministic typography later.

Do not use it for:

- Technical infographics, diagrams, architecture maps, or data visualization where precision matters more than atmosphere.
- Logos, icons, UI mockups, or assets that should remain editable vectors.
- Literal terminal art made from readable characters.
- Photorealistic editorial photography unless the brief explicitly asks for a hybrid.

Pair with `web-design` when the image must integrate into a broader page system, card grid, article template, or responsive layout.

## Core Visual Grammar

### 1. Marks model form

The defining trait is **form-modeling square-cell texture**:

- Fine, dense square marks follow cloud volume, mountain planes, water ripples, vegetation, fabric, stone, or machinery.
- Cell density increases in shadow, material detail, and focal edges; it opens in atmospheric distance and quiet regions.
- Ordered-dither patterns bridge posterized tonal bands instead of floating above them.
- Marks may vary in size and spacing, but they should read as one authored system.
- The image must still have convincing large shapes when blurred or viewed from a distance.

Reject outputs where dots are evenly sprayed over the frame, forms remain clean vectors underneath, or texture disappears completely at card size.

### 2. Painterly masses beneath the cells

Build the scene from broad, legible masses before microtexture:

- clear foreground, middle distance, and background
- simplified oil-like planes rather than photographic detail
- strong light direction and colorful reflected light
- atmospheric depth without lens blur or bokeh
- tactile canvas, ink, or print character without fake paper clutter

The best result reads first as a composed painting, then rewards closer inspection as dithered computer art.

### 3. Limited luminous palette

A proven palette family is:

- deep cobalt and ultramarine for stable structure
- cyan used selectively for illuminated cool edges
- emerald, dark teal, and forest green for depth and shadow
- burnt orange and coral for energy or focal contrast
- peach, warm cream, and ivory for light

Use colorful blue-green shadows rather than neutral gray. Keep the palette limited enough to feel authored. Do not default to purple-blue AI gradients, neon cyberpunk glow, or a rainbow of unrelated accents.

This palette is a starting point, not a universal law. Adapt hue emphasis to the subject while preserving coherent temperature and tonal separation.

### 4. One physical metaphor

Abstract topics still need a concrete image. Prefer one solid metaphor with an observable silhouette:

- a flywheel, staircase, workshop, observatory, bridge, garden, archive, kiln, loom, vessel, terrace, or accumulated craft
- a lone traveler, maker, machine, or structure at human-readable scale
- a landscape whose spatial relationship carries the argument

For AI, agents, data, or systems topics, do not automatically draw blue nodes and edges. Network graphs, constellation webs, data beams, circuit paths, glowing routes, wireframe objects, and device-to-device links are common generic completions. Use them only when the subject specifically requires a network and the brief accepts that visual language.

### 5. Hierarchy survives every crop

The image needs:

- one dominant subject or spatial event
- a simple silhouette that remains recognizable when small
- edge detail that enriches rather than competes
- a quiet area for optional typography
- meaningful content inside every required crop safe area

Do not assume a strong 16:9 frame will survive a square, portrait, or centered card crop. The image contract is the set of actual rendered crops, not the native canvas alone.

## Define the Image Contract

Before prompting, write:

```text
Purpose: article cover / card thumbnail / social preview / replacement
Message: the one idea the image must communicate
Audience and tone: who sees it and what they should feel
Primary metaphor: one physical subject or scene
Text policy: strictly textless / deterministic overlay later / exact embedded copy
Source aspect: preferred native aspect ratio and minimum dimensions
Rendered crops: exact card, hero, mobile, Open Graph, and social shapes
Focal safe area: region that must retain the subject
Style references: each image labeled by role
Preserve: palette, lighting, texture, atmosphere, crop hierarchy
Remove: rejected motif and all visually adjacent cues
Strict exclusions: content, styles, providers, or file types that are unacceptable
```

If the topic is not known yet, create a standalone scenic study with a clear focal hierarchy and a calm text-safe region. Do not pretend an arbitrary metaphor represents a future article.

## Workflow

### 1. Inspect the real use surface

Before generating:

1. Read the image metadata and rendering contract.
2. Inspect the hero, list card, mobile card, and social metadata paths.
3. Record actual container aspect ratios, `object-fit`, and `object-position` behavior.
4. Capture representative existing images at their rendered sizes.
5. Identify whether text is in the bitmap or rendered separately.

Completion criterion: every required output size and crop behavior is known; no crop is being guessed from a filename.

### 2. Analyze references as visual grammar

Use two or three approved references when available. For each, identify:

- composition and focal hierarchy
- subject scale and negative space
- palette and light direction
- where cell density increases or dissolves
- how marks describe specific materials
- which traits survive at thumbnail size
- any unwanted motifs, text, borders, or UI cues

Label each input as one of:

- **Style reference:** texture, palette, atmosphere, mark behavior.
- **Composition reference:** massing, crop, subject scale, safe area.
- **Edit target:** an image whose actual pixels should be changed.

Do not tell a generator to “edit” a reference when the user wants a new scene in the same visual family.

Completion criterion: the prompt can name observable traits instead of saying only “make it similar.”

### 3. Pass the concept gate

State the topic as one sentence, then propose one to three physical metaphors. Evaluate each on:

- semantic fit
- silhouette clarity
- novelty without obscurity
- crop resilience
- compatibility with painterly massing
- distance from rejected clichés

For a replacement cover, separate the existing image into two lists:

```text
PRESERVE: palette, light, texture, density, atmosphere, crop behavior
REMOVE: rejected object plus near-neighbor cues that recreate the same reading
```

If the user rejects network imagery, `REMOVE` must include not only nodes and edges but also constellation dots, dotted trajectories, data beams, glowing routes, circuit traces, and wireframe structures.

When exploring alternatives, generate isolated directions rather than combining three metaphors into one busy compromise.

Completion criterion: one metaphor has a clear reason to represent the article and a concrete avoid list.

### 4. Write a structured generation prompt

A strong prompt describes scene, composition, material behavior, palette, exclusions, and deliverable. Use this template:

```text
Create ONE finished native raster image for an editorial cover.

PURPOSE AND IDEA
[Article or asset purpose.] The image should communicate [single message] through
[one physical metaphor]. It should feel [emotional target], not [mismatched tone].

SCENE
[Concrete foreground, middle distance, background, subject, action, and light.]

COMPOSITION
- [Required aspect ratio and focal safe area.]
- Strong foreground / middle distance / background separation.
- One dominant silhouette or spatial event.
- Keep [text-safe region] comparatively calm without making it blank.
- Concentrate supporting texture toward [edges / lower third / subject materials].
- No presentation-board frame.

VISUAL GRAMMAR
- Vintage dithered oil-painting or travel-poster massing translated through
  late-1980s/early-1990s computer graphics and printmaking.
- Fine, dense, visible square-cell stippling, ordered-dither clusters,
  pointillist marks, and posterized tonal bands must MODEL FORM and lighting.
- Marks follow cloud volume, object planes, water, vegetation, stone, fabric,
  or machinery rather than forming a uniform overlay.
- Painterly oil-like masses beneath the cells; tactile canvas and ink character.
- Limited palette: cobalt, ultramarine, dark teal, emerald, selective cyan,
  burnt orange, coral, peach, warm cream, and ivory.
- Colorful blue-green shadows, not neutral gray.
- Detailed at full size but immediately readable as a thumbnail.

STRICT EXCLUSIONS
- [Rejected motif and every adjacent cue.]
- No photorealism, glossy 3D, smooth airbrushed gradients, clean flat vectors,
  anime, low-texture concept art, generic purple AI glow, bokeh, or lens effects.
- No borders, UI cards, diagrams, interface chrome, captions, or microtext.
- No glyph-like texture, pseudo-writing, or accidental readable characters. If
  embedded generated text is explicitly selected, only the exact approved copy
  may be readable; all other text remains forbidden.
- [Text policy from below.]

DELIVERABLE
- Invoke native raster image generation and produce the actual image file.
- Preserve the maximum-resolution native output.
- Do not return only a prompt or description.
- Do not substitute SVG, HTML, Canvas, or procedural drawing unless requested.
```

Completion criterion: the prompt names the exact scene, composition, form-modeling mark behavior, palette, text mode, exclusions, crop contract, and real raster deliverable without relying on hidden context.

### 5. Enforce the text policy

Choose exactly one mode.

#### Strictly textless

The prompt must forbid:

```text
No text, letters, numbers, logos, signs, labels, symbols, watermark,
pseudo-writing, ghosted typography, erased typography, or readable glyphs anywhere.
```

“No text” is literal. A faded word, fake sign, tiny label, watermark, or glyph-like texture fails.

#### Deterministic title overlay

Generate the art textless, then add the exact title in HTML, CSS, SVG, or the publishing system. This is the default when spelling, accessibility, localization, or responsive wrapping matters.

- Keep meaningful text out of the generated pixels.
- Use a large heavy sans-serif or the established editorial type system.
- Verify line breaks in every crop.
- Preserve contrast with a quiet tonal region, subtle shadow, or controlled overlay rather than a decorative plate.

#### Embedded generated text

Use only when the bitmap itself must contain lettering and exact reproduction can be verified. Treat every spelling and punctuation error as a failed image.

Completion criterion: exactly one text mode is selected, its prompt constraints are explicit, and any required copy can be verified character for character in every rendered crop.

### 6. Generate through an approved native-raster path

Use the user's named provider or established first-party workflow when one exists. Do not silently switch to an unfamiliar keyless service, a different model family, or deterministic vector/procedural artwork merely because generation is temporarily unavailable.

Requirements:

- Generate an actual bitmap, not a prompt-only response.
- Preserve native output before resizing or compressing.
- Upload only references the user owns, is permitted to share, and has authorized for the selected provider; nonpublic assets require explicit approval before upload.
- Keep secrets, account data, private messages, precise location, and other undisclosed information out of prompts and reference files.
- Check the provider's current retention, training, and rights terms before sending sensitive or licensed material.
- Remove GPS, identifying EXIF, and other unnecessary metadata from upload copies while preserving an untouched authorized source locally when required.
- Keep scratch prompts and references outside the product repository. Commit only the approved public artifacts and documentation, and delete temporary sensitive copies according to the agreed retention policy.
- Keep approved prompts and references with the private job record when provenance matters; do not make that archive public by default.
- Use one scratch workspace per concept during parallel exploration.
- If a provider reports a temporary cap with a reset time, preserve the exact approved prompt and references and retry after reset rather than silently downgrading.
- If the approved path is persistently unavailable, report the blocker and obtain approval before changing execution strategy.

When Codex CLI with built-in image generation is the approved path, run it inside a scratch Git repository with a real raster deliverable in the prompt:

```bash
codex --enable image_generation exec \
  --sandbox workspace-write \
  -C /path/to/scratch-repo \
  - -i /path/to/style-reference.png \
  < /path/to/prompt.txt
```

CLI flags and output locations change. Verify against the installed tool rather than assuming this adapter is universal.

Completion criterion: the native raster exists at a known path and its format and dimensions were read from the actual file.

### 7. Review full frame and rendered crops

Inspect the actual pixels, not the prompt or generator description.

#### Full-frame gates

- The primary metaphor is immediately identifiable.
- Painterly foreground/midground/background massing is clear.
- Square-cell marks model volume and material.
- The palette is coherent and shadows remain colorful.
- The frame contains no forbidden motif, accidental text, watermark, border, UI, or pseudo-writing.
- Texture is detailed without becoming uniform noise.

#### Crop gates

Create or capture every real crop:

- native or article hero
- `1200×675` Open Graph / 16:9 derivative when applicable
- exact list-card container, including its actual `object-fit` and `object-position`
- narrow mobile card or hero
- square or portrait social crops if the product uses them

If a card uses a centered 5:4 crop, inspect that exact crop. Do not approve from the 16:9 frame and assume the subject survives. At least the primary metaphor and one supporting spatial cue should remain visible.

Judge the image at the rendered card dimensions. Zoomed-in beauty is not evidence of thumbnail readability.

Completion criterion: every required crop preserves the intended reading with no accidental exclusion violation.

### 8. Iterate with one targeted change

When an output is close, preserve accepted traits and change one dimension:

- subject scale
- focal placement
- texture density
- palette balance
- central calm area
- unwanted motif
- crop-safe positioning

Do not respond to a rejected metaphor by vaguely asking for “less of it.” Remove the object and its complete supporting visual vocabulary.

For larger replacement work, produce up to three isolated directions, review full frame and crops, and choose on semantic fit and site cohesion rather than novelty alone.

Completion criterion: the accepted traits remain intact, the requested change is isolated and visible, and the candidate has passed the same full-frame and crop gates as the original.

### 9. Integrate and publish safely

- Keep the native raster and create a separate optimized derivative.
- Use versioned filenames for replacements so caches and social cards converge on new bytes.
- Update the consuming metadata and rendering path rather than copying an orphaned file.
- Confirm intrinsic dimensions or aspect ratio are reserved to avoid layout shift.
- Give the image truthful alternative text when it conveys information; use empty alt only when it is genuinely decorative and nearby text carries the same meaning.
- Verify article, card, mobile, Open Graph, and social metadata outputs.
- For a deployed replacement, compare the production asset bytes or checksum with the approved local derivative and inspect the live rendering.

Completion criterion: the approved image, not a stale cached predecessor, is rendered in every intended production surface.

## Review Rubric

An image passes only when every hard gate passes.

| Area | Pass condition |
| --- | --- |
| Concept | One physical metaphor clearly supports the subject. |
| Composition | Large masses and focal hierarchy survive all required crops. |
| Mark behavior | Fine square cells describe form, light, and material rather than acting as an overlay. |
| Palette | A limited luminous system uses colorful shadows and controlled warm/cool contrast. |
| Text | The selected text policy is followed exactly. |
| Exclusions | No rejected motif or near-neighbor cue returns. |
| Thumbnail | The image remains legible and distinctive at actual card size. |
| Artifact | A verified native raster and required derivatives exist. |
| Integration | Correct image bytes and metadata render on every target surface. |

Reject a beautiful image when it violates the semantic constraint. Vibe does not outrank meaning.

## Common Failure Modes

1. **Flat vector plus dot filter.** Re-prompt so marks follow planes, contours, and light; require painterly masses beneath them.
2. **Literal ASCII characters.** Clarify that ASCII-like means square-cell rhythm only and ban readable glyphs.
3. **Generic blue network graph.** Replace the metaphor with a solid physical subject and ban every adjacent network cue.
4. **Smooth modern concept art.** Strengthen posterized bands, old-print material, ordered dithering, and limited palette constraints.
5. **Texture overwhelms hierarchy.** Quiet the focal safe area and move dense marks toward materials, shadows, and edges.
6. **Strong wide frame, failed card crop.** Recompose for the real crop rather than shifting CSS blindly.
7. **Generated title errors.** Return to a textless background and deterministic typography.
8. **Provider substitution.** Preserve the accepted path or ask before changing it; do not present a procedural fallback as equivalent.
9. **Prompt-only completion.** The deliverable is the raster file plus verified derivatives, not the prompt.
10. **Overwriting a live filename.** Publish a versioned asset and update metadata so caches cannot hide the replacement.

## Verification Checklist

- [ ] Purpose, message, audience, metaphor, text policy, and rendered crops are explicit.
- [ ] References are labeled by role and translated into observable visual grammar.
- [ ] Reference rights, upload authorization, provider retention terms, sensitive metadata, and scratch-file retention were checked.
- [ ] No private prompt, reference, or scratch artifact is staged for publication.
- [ ] Preserve/remove lists exist for replacement work.
- [ ] The concept avoids unsupported category clichés.
- [ ] Native raster generation produced a real file.
- [ ] Native format and dimensions were verified from the file.
- [ ] Fine square-cell marks visibly model form and lighting.
- [ ] Painterly massing and focal hierarchy survive a squint test.
- [ ] Palette and shadow color are coherent.
- [ ] No accidental text, glyphs, logo, watermark, border, UI, or rejected motif is visible.
- [ ] Hero, Open Graph, card, mobile, and other real crops were inspected.
- [ ] Thumbnail readability was judged at rendered size.
- [ ] Native output is preserved separately from optimized derivatives.
- [ ] Replacement assets use versioned filenames.
- [ ] Metadata, accessibility text, layout dimensions, and production bytes were verified.
