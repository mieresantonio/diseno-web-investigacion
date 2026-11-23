# Showcase design system — one-page summary (English)

One-page English summary of `sistema-diseno-vitrina.md`, the full
reference (in Spanish). If the two disagree, the Spanish document
wins. Nothing here goes beyond what that document says.

## What it is

A quantified design system for showcase interfaces: panels,
landings, CRUD apps and portfolios. Distilled on 7 November 2026
from the design system preloaded in Grok Build, inspected
first-hand in the exported workspace of the app "Factory · Estudio ·
Currículum". Principles, parameters and motion recipes were
extracted — method, not work — and rewritten in this repo's own
words. Its operating skill is `diseno_vitrina`.

## Rule one: system before style

No loose value ever reaches a component. Before styling any
screen, one single place defines the semantic palette
(background, surface, raised, text, muted text, border, accent),
the radius, spacing and type scales, and the motion tokens (in
Tailwind v4, the `@theme` block; elsewhere, root variables). A
value with no token or scale step is not used. Components start
from accessible primitives (shadcn/Radix style) dressed with
the tokens.

## Tokens

**Spacing:** 4, 8, 12, 16, 24, 32, 48, 64 px. Nothing off the
scale. **Radii:** 4, 8, 12, 16, 24 px; full pill (9999) only
for chips and small buttons. **Fluid type** with `clamp()`:
XS about 0.75–0.81 rem, S 0.875–0.94, base 1–1.06, L 1.125–1.25,
XL 1.5–2, 2XL 2–3, 3XL 2.5–4. Line height: 1.1 large headlines,
1.25 titles, 1.5 body. Tracking: −0.02 em large text, −0.03 em
cover headlines. **Motion:** micro 80 ms, close and in-place
changes 150 ms, main openings 250 ms, panel exits 350 ms,
content reveal 400 ms, rare emphasis 500 ms, list stagger
40 ms. Main ease-out curve: `cubic-bezier(0.22, 1, 0.36, 1)`.
Entry distances 4–12 px. Opening scales: modals from 0.96,
menus from 0.97, tooltips from 0.98 — never from 0.

## Colour discipline

Neutrals cover 90% or more of the surface: near-white or
near-black backgrounds, quiet greys, borders derived from the
text colour as translucents (they adapt to light and dark on
their own). One single accent family, reserved for the primary
action and focus. Banned as brand accent unless expressly
commissioned: purple, violet, magenta, yellow, gold, orange.
Gradients only when nearly invisible (luminosity jump of 8% or
less). Icons in monochrome or `currentColor`. Semantic states
in contained green, amber and red: badges and small icons only,
never whole panels. AA contrast on body text.

## Radii, surfaces, type

**Concentric radii, mandatory:** outer radius = inner radius +
padding between them; each nesting level drops one scale step.
The same radius on parent and child is the most common silent
defect. **Shadow instead of border** on cards and buttons: the
shadow adapts to any background, a solid border does not. Light
recipe: 1 px ring at 6% black + soft 1–2 px shadow at 6% + 4 px
ambient at 4% (on hover, 8/8/6%); in dark mode the white ring
at 8% is enough (13% on hover). Dividers stay borders: they
separate, they do not lift. Images with a 1 px inner outline at
10%. Optical alignment: on a button with text + icon, the icon
side carries about 2 px less padding. Minimum touch area
44 × 44 px (40 as floor). **Type:** one family with weight
contrast, or a sober pair; never more than two families; mono
only for code, figures and identifiers. Weights: headlines
500–600, body 400, buttons 500–600; no 900 black on large text.
At most three effective sizes per screen. Live figures with
`tabular-nums`. Reading width 60–75 characters.

## Motion

Prefer interruptible CSS transitions; keyframes only for
one-off staged sequences. Enumerate the properties (`opacity,
transform`, blur only if needed): `transition: all` is
forbidden. Enter slower than exit: opening 250 ms, closing
150 ms. Nothing enters from scale 0; menus grow from their
trigger, modals from the centre. Everything respects
`prefers-reduced-motion` (opacity only, or instant). Durations
live in CSS variables so the orchestrating JS reads the same
values. The full recipe catalogue is in §7.

## Anti-slop

No emoji as icons; no gradient masses or glows as filler; no
hand-drawn SVG illustrations; no grey "placeholder" boxes in the
finished product; no default font without hierarchy; no frosted
glass in chain, rainbow borders or neon shine; no magic values;
no bounce on every control. Every element earns its place or
gets cut. Empty, loading and error states are part of the design.

## Verification

Nothing is declared "done" without looking at its own work: a
two-window smoke pass (desktop 1280×800, mobile 390×844) with a
structured verdict — HTTP status, console and page errors,
horizontal overflow, text length — where the screenshots are
read with eyes, not filed unseen; a pass against the build; and,
when the app has something to operate, an interactive pass that
asserts the result with a check that fails out loud. Every
published app carries its link card (1200×630) and a crisp SVG
favicon at 16 px. The closing checklist is §12.

## What this distillation does not transfer

The model's trained taste (the generative prior that places the
first draft well when no template fits), its built-in image
tools, and its internal preview loop. This system covers "mould"
design (panels, landings, CRUD, portfolios). Art direction from
scratch stays the territory where Grok keeps the edge, rented
with its tokens when a project asks for it.

---

*Summary written 23 November 2026 from a first-hand reading of
`sistema-diseno-vitrina.md` (distilled 7 November 2026).*
