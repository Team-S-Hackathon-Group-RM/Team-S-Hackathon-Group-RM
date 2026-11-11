# Hospitalisation estimates from generative AI (metric sheet: 'ask different AIs')

Asked on 11 Nov 2026, same prompt to each model independently, no web access.

Prompt: *A US town survey (adults 18+). Everyone will be infected with COVID-19 (100% infection). Give (1) P(hospitalised | infected, unvaccinated, no chronic conditions) for age groups 18-34, 35-44, 45-54, 55-64, 65+; (2) vaccine effectiveness against hospitalisation; (3) a per-condition multiplier for each additional chronic condition. State the period/variant assumed and sources.*

| Source | 18-34 | 35-44 | 45-54 | 55-64 | 65+ | Vaccine effectiveness | Per chronic condition |
|---|---|---|---|---|---|---|---|
| Claude Sonnet 5.5 (asked separately, same prompt) | 0.010 | 0.018 | 0.030 | 0.055 | 0.140 | 0.80 | ×1.8 |
| Claude Haiku 5.5 (asked separately, same prompt) | 0.006 | 0.012 | 0.025 | 0.050 | 0.120 | 0.85 | ×1.6 |
| Claude Fable 5.2 (asked separately, same prompt) | 0.012 | 0.025 | 0.045 | 0.080 | 0.200 | 0.85 | ×1.5 |
| **Used (average of the 3)** | 0.0093 | 0.0183 | 0.0333 | 0.0617 | 0.1533 | 0.833 | ×1.633 |


Period assumed by all three: pre-Omicron (wild-type to Delta). Caveats given: values recalled from memory, roughly ×2 uncertainty on hospitalisation rates; the per-condition multiplier is the least certain; cap the probability for many conditions.


*The team may add further rows (e.g. Gemini, ChatGPT asked by other members) and re-average.*
