# Master-detail content experiences

Use this reference when designing a notes library, bookmark organizer, inbox, catalog, documentation browser, media log, knowledge base, or any surface where users move from broad collections to a scannable list and then to richer item detail.

The pattern has three information layers:

```text
collection navigation → item list → selected item detail
```

The layers should preserve orientation rather than behave like three unrelated pages. Desktop can show all three at once. Mobile should preserve the same route and data semantics while replacing the cramped layout with a focused full-screen step.

## Product read

Before choosing panes, define:

- What is being collected?
- Is the primary behavior browsing, retrieving, triaging, comparing, or reading?
- Which item types are homogeneous and which need richer typed details?
- Which metadata is essential in a row, and which belongs only in detail?
- Should a user be able to share, reload, bookmark, or use Back on a selected item?
- Is there a useful aggregate view such as All items, or must users always choose a collection first?
- Which parts of the experience are public, private, editable, or source-attributed?
- What happens when a result has no rich detail and should open its source instead?

Do not begin with a three-column screenshot. Begin with the information and navigation contract.

## Information architecture

### Use a broad default when discovery matters

A first collection such as **All items** or **All links** can reduce category guessing and make recent additions immediately visible.

Use an aggregate default when:

- people often browse before knowing the category
- the same item may be found through several mental models
- chronological recency matters
- collection counts are small or uneven
- newly captured material should be visible without another navigation step

Do not add an aggregate merely because it is common. If collections represent strict security, workflow, or ownership boundaries, a broad view may be confusing or inappropriate.

An aggregate route needs one explicit resolution rule. Decide whether detail URLs remain contextual to the aggregate or redirect to the item's canonical collection. Reuse that rule in server validation, client lookup, metadata, and generated routes.

### Treat collection order as navigation policy

Collection order changes what users see first and which mental model the product teaches. Keep one authoritative order declaration and test it. Do not independently reorder desktop navigation, mobile navigation, data fixtures, and generated routes.

A practical sequence often begins with the broad archive, then action-oriented collections, then specialized or lower-frequency types. The brief outranks this default.

### Model typed records without bloating every row

A content library may contain links, books, films, people, design references, skills, or original notes. Give shared fields a small common contract and keep type-specific detail structured.

```text
shared: id, slug, collection, title, rowNote, source, addedAt, status
optional detail: summary, sections, progress, author, director, year, cast,
poster, score, tags, takeaways, workflow, related links
```

Use one pure rule such as `itemHasDetails(item)` to determine:

- whether the row opens internal detail or an external source
- whether a detail route is valid
- whether static route parameters are generated
- whether a disclosure affordance appears
- whether client selection can resolve the item

A route should never return item-specific metadata with a generic or empty body. Detail eligibility is a data and routing contract, not a visual guess.

## Row design

Rows exist for scanning and retrieval, not to preview the entire record.

A strong row usually contains:

1. a quiet type cue when needed
2. the title
3. at most one author, creator, source, or useful descriptor
4. one short user note or status line when it materially helps

Keep source, type, collection, tags, status, date, author, and description from appearing simultaneously unless operational density truly requires it.

Use typography, alignment, and subtle separators before card shells. A notes list often benefits from calm rows rather than a grid of rounded cards. Selection should be visible but quiet, and clearly different from hover.

Requirements:

- selected text and geometry stay stable
- use `aria-current="page"` for the open route when appropriate
- keep the selected row mounted while detail is open on wide screens
- long titles and unbroken URLs wrap safely
- missing media does not collapse row height unpredictably
- decorative type icons are hidden from assistive technology when the link already has a complete accessible name
- external-link behavior is conveyed accessibly rather than only through an icon

If a user's own short note is part of the record, preserve its wording with light cleanup. Do not replace a simple observation with generic productivity language.

## Desktop composition

A wide layout can preserve all three layers:

```text
collection rail + gap + flexible list + gap + contextual detail panel
```

### Collection rail

- Use a real navigation landmark with a useful label.
- Keep collection names and counts stable.
- Make current location visible without changing weight or padding.
- Sticky positioning is appropriate only if the rail remains fully reachable at short viewport heights and zoom.
- Do not make the rail so wide that it starves the list and detail columns.

### List pane

- Give the selected collection a clear heading and concise description only when it adds meaning.
- Keep search and filters close to the results they affect.
- Announce result counts when filtering changes them if that feedback is not otherwise obvious.
- Let the list own scrolling only when nested scrolling is clearly better than document scrolling.
- Preserve the selected row during detail navigation so users retain spatial context.

### Detail panel

- Treat detail as a distinct article or complementary region.
- Keep the collection rail and list visible; do not replace the list on desktop unless the task requires maximum reading width.
- Align the panel's start with the list content, not arbitrary viewport chrome.
- Reserve enough width for prose, media, and structured facts without making the list unusably narrow.
- Use a dedicated Back or Close action only when it has clear semantics; do not add a decorative chevron that duplicates browser navigation ambiguously.
- Rich records can show poster, cast, progress, score, structured steps, or takeaways here while their rows remain compact.

A three-column layout should feel like stable navigation plus changing context, not three equal cards.

## Tablet and collapse region

Do not jump directly from a generous desktop frame to a 320px mobile stack. Test the widths where the third panel first becomes cramped.

Possible transitions:

- collapse the collection rail into a collection picker while keeping list and detail
- keep the collection rail and list, but make detail a route-level replacement
- use a two-pane list/detail layout with collection navigation above

Choose based on content width, not device labels. Avoid a narrow detail drawer when the content contains long prose, media, tables, or structured facts.

At one pixel below and above each breakpoint, verify that no important control disappears, no selected state becomes ambiguous, and browser history semantics stay unchanged.

## Mobile composition

On narrow screens, preserve the information sequence rather than squeezing all panes together:

```text
collection index → collection list → full-screen item detail
```

A rich detail should normally be a full-screen route-level replacement with an explicit Back action. This is better than a modal or thin drawer when the content is primary, scrollable, shareable, or directly loadable.

Mobile requirements:

- direct detail URLs render complete content
- the heading moves into the first viewport without being hidden by sticky chrome
- Back returns to the correct collection and selected row when history supports it
- a directly loaded detail has a safe fallback instead of backing out of the product unexpectedly
- focus moves to the new view's heading after an in-app replacement
- returning focus lands on the previously selected row when it exists
- the list does not remain interactable behind the detail
- scroll position is restored intentionally, not accidentally
- poster, note, score, metadata, and bottom-of-page controls are checked below the fold

Do not approve a long detail page from a header-only screenshot.

## URL and history semantics

Shareable selection belongs in the URL. Treat routing as part of the component design.

A robust contract defines:

- collection route
- supported item-detail route
- unsupported detail behavior
- direct-load behavior
- in-app open behavior
- explicit Back behavior
- browser Back/Forward behavior
- aggregate item resolution
- canonical metadata and social sharing behavior

Use the framework router by default. Use native `pushState()` or `replaceState()` inside a framework application only when current framework documentation explicitly supports that integration or provides a state-extension mechanism.

- never replace, spread, copy, or reinsert opaque framework-owned `history.state`
- if supported custom state is unavailable, keep navigation provenance outside framework-owned history state and use the collection fallback
- in a router-neutral native History flow, put one app-owned parent marker on the current detail entry when it is pushed from a known collection
- call `history.back()` only when the current detail entry carries that marker, which certifies a known parent; otherwise replace it with the safe collection fallback
- replace a direct-loaded entry with the fallback rather than pushing another detail/index loop
- test direct load, in-app open, explicit Back, browser Back/Forward, and a subsequent normal framework navigation

Route metadata and rendered UI must agree. Invalid item routes should produce a real not-found state rather than a 200 page with stale or generic content.

## Focus and accessibility

Use structural landmarks:

- one page-level `<main>` only
- labeled navigation for collections
- labeled region for the selected collection/list
- complementary region or article for contextual detail
- real buttons for actions and links for navigation
- a real grouping role and label around search/filter controls

Focus behavior differs by viewport:

### Desktop

- Opening detail keeps focus on the selected row so context remains stable.
- Closing detail restores focus to that row if the focused close control unmounts.
- Initial render does not steal focus.

### Mobile

- Opening a collection or detail moves focus to the new `h1`, commonly with `tabIndex="-1"` for programmatic focus.
- Returning to a list restores focus to the selected row.
- If the row cannot be resolved, focus the collection heading as a safe fallback.
- `popstate` transitions follow the same focus model as explicit in-app navigation.

The visual order, source order, focus order, and reading order should agree at every layout.

## Search, filters, and sorting

Search and filters should belong to the current list context.

- Label the search field with the noun being searched.
- Decide whether filters are URL-backed, durable preferences, or local transient state.
- Preserve query state across detail open/close when users expect to return to the same result set.
- Keep selected items resolvable even when a filter changes; define whether detail closes, remains visible, or shows that the item is outside the current results.
- Announce empty results and provide a clear reset.
- Avoid filter pills for every facet by habit; use the control form that matches cardinality and frequency.

Sorting must reflect collection meaning:

- chronological archives: date descending before month grouping
- action lists: workflow/status priority, then date
- scored media: explicit user choice or a clearly labeled default
- alphabetical reference libraries: locale-aware title or creator order

Do not reuse one status-first comparator for a chronological archive; grouping can become silently wrong.

## Visual treatment

For a clean editorial notes surface:

- prioritize type hierarchy, spacing, and alignment
- use cards only when grouping or elevation genuinely needs a boundary
- keep row separators and selected fills subtle but visible in every theme
- align counts and scores with tabular figures
- bound poster/media with a quiet surface treatment
- reserve accent color for current selection, links, and meaningful status
- keep descriptive copy short enough that navigation remains scannable
- avoid large marketing-page headers above an operational content browser
- make loading, empty, missing-media, and unsupported-detail states feel like part of the same system

A simple interface is not an unfinished interface. It still needs exact focus, history, route, and responsive behavior.

## Motion and optional sound

Use motion for continuity between list and detail, not as decorative entrance choreography.

- A selected-row treatment can settle immediately or with a short color transition.
- A desktop detail panel may enter from the direction of the list if that reinforces spatial continuity.
- Mobile route replacement should acknowledge input promptly and remain interruptible.
- Reduced motion removes large travel while preserving visible state change.
- Wait past the longest transition before judging persistent blur, opacity, or transform defects.

If the product already has an opt-in interaction-sound system, reuse it for user-initiated internal transitions. Do not add a parallel audio stack, bypass preference, autoplay sound, or play cues on browser Back/Forward. Sound can reinforce a transition but cannot be its only feedback.

## Data and privacy boundary

When private inboxes, DMs, email, or bookmarks feed a public content browser, keep an explicit private archive and smaller public projection.

Public records should contain only public URLs, public attribution, concise summaries, and wording known to be safe. Exclude raw messages, sender/recipient IDs, private timestamps, cookies, browser state, and conversation metadata.

Treat public dates as a separate contract. A public projection date is not automatically the private capture or message time.

Sanitize every content URL before rendering. Allow only the schemes and same-origin paths the product supports. Locally host third-party media when remote rendering would leak visitor information or break provenance requirements.

These are product and trust constraints, not merely backend concerns. The interface should not imply a source, watch date, score, status, or detail that the data does not actually establish.

## Testing strategy

Use layered tests.

### Pure contract tests

- collection order and aggregate placement
- item detail eligibility
- item resolution from aggregate and canonical collections
- valid and invalid route parameters
- row-copy limits and descriptors
- sorting and month grouping
- URL sanitization

### Component tests

- selected row remains mounted
- `aria-current` and accessible names
- search/filter result and empty behavior
- internal versus external row action
- focus targets for open and close
- reduced-motion behavior

### Browser tests

- direct collection and detail loads
- unsupported detail not-found behavior
- in-app open, explicit Back, and browser Back/Forward
- query/filter preservation
- focus movement and restoration
- desktop three-layer balance
- tablet collapse behavior
- true 375px and 320px route replacement
- 200% zoom and keyboard-only paths
- no page-level horizontal overflow
- clean console and network behavior
- top and below-the-fold detail content

A screenshot cannot prove history, focus, route validity, or selected-row persistence. Exercise those behaviors directly.

## Common failure modes

1. **Three columns chosen before the information contract.** Define layers, routes, and typed details first.
2. **Rows carry every field.** Move rich metadata into detail and preserve scan rhythm.
3. **Detail replaces the list on desktop.** Keep the selected row and list visible when width permits.
4. **Mobile uses a cramped drawer.** Use a full-screen route replacement for primary scrollable content.
5. **Aggregate and canonical routes disagree.** Centralize item resolution.
6. **Detail metadata without detail UI.** Generate only routes that the same eligibility rule can render.
7. **Framework history state is copied.** Store only app-owned markers.
8. **Back always calls `history.back()`.** Direct loads need a safe fallback.
9. **Focus stays in unmounted UI.** Move or restore focus intentionally by viewport.
10. **Selected and hover look identical.** Give current route a persistent, stable treatment.
11. **A long detail is approved from its header.** Inspect the full content and bottom actions.
12. **Collection order drifts.** Keep one source of truth and a regression test.
13. **All items is added without a resolution model.** Define contextual or canonical detail behavior first.
14. **Private capture metadata leaks publicly.** Use a deliberately smaller projection schema.

## Verification checklist

- [ ] Product read defines content types, primary task, route needs, and aggregate behavior.
- [ ] Collection order has one source of truth.
- [ ] Shared row data and typed rich detail are separated.
- [ ] One pure eligibility rule governs affordance, routing, params, and rendering.
- [ ] Rows remain minimal and selected geometry stays stable.
- [ ] Desktop preserves collection, list, selected row, and detail context.
- [ ] Tablet behavior is tested through the actual collapse range.
- [ ] Mobile uses a complete route-level detail with safe Back behavior.
- [ ] Direct loads, unsupported routes, and browser history behave correctly.
- [ ] Aggregate item resolution is shared across server and client paths.
- [ ] Focus movement and restoration match desktop and mobile semantics.
- [ ] Search, filters, sorting, empty states, and query persistence are defined.
- [ ] One `<main>` and correctly labeled navigation/list/detail landmarks exist.
- [ ] Reduced motion preserves understandable state changes.
- [ ] True 320px, 375px, breakpoint boundaries, desktop, wide desktop, and zoom were checked.
- [ ] Full long-form details, including below-the-fold content, were inspected.
- [ ] Console, network, overflow, and accessibility paths are clean.
- [ ] Public/private boundaries and rendered claims remain truthful.
