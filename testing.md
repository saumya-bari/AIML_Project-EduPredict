# Design Decisions and Rationale
1. CLI-first execution satisfies command-line usability.
2. Synthetic data avoids exposing real student information.
3. Random Forest handles nonlinear tabular patterns and provides feature importance.
4. Modular files separate responsibilities and simplify testing.
5. CSV is portable and sufficient for this prototype.
6. Validation prevents out-of-range inputs.
7. Fixed random seed makes demonstrations reproducible.
8. Model and metrics are saved as generated artifacts.
