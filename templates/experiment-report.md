# Experiment: <specific question>

- Date / author:
- Repository revision / command:
- Environment / hardware:
- Data version, permissions and split manifest:
- Seed(s):
- Compute budget and stopping rule:

## Question

State one measurable hypothesis before running the experiment.

## Baseline and change

Describe the baseline, the one intended change, and what is held constant. Explain any unavoidable differences.

## Evaluation protocol

Define the metric, thresholds, aggregation, held-out population, and leakage checks. Select hyperparameters using training/validation data only.

## Results

| Variant | Validation metric | Final test metric | Latency / memory | Budget |
| --- | --- | --- | --- | --- |
| Baseline | | | | |
| Change | | | | |

Report repeated runs or uncertainty where the claim needs them. Label incomplete or differently budgeted comparisons explicitly. Include absolute numbers, not only percentage gains.

## Failure analysis

Include representative errors, relevant slices, and a case where the change made performance worse.

## Conclusion

Does the evidence support the hypothesis? What remains untested? What would the next experiment resolve?
