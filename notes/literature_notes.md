# Notizen für Literatur in Masterarbeit

## Buch: V+V für die Simulation in P und L

- Tracing Analyse für die Einzelverfolgung von Aufträgen durch die Factory

## Paper MODULAR VALIDATION WITHIN DIGITAL TWINS: A CASE STUDY IN RELIABILITY

- Das Paper verwendet ein zweistufiges Modell zur Validierung von DT. Im ersten SChritt wird das Modell historisch und Face to Face validiert. Im zweiten Schritt werden Modellmodule gebildet, die dann entweder fixiert werden oder je nach Diskrepanz neu angepasst werden:

Algorithm: ModularValidation
Input: stochastic_petri_net_model, event_log, validation_policy, discrepancy_threshold, recalibration_threshold
Output: recalibrated_or_re_extracted_submodels

1. Calculate the frequency of occurrence of each transition in the stochastic_petri_net_model.
2. For each transition:
    - If the transition occurs frequently, flag it for preservation.
    - Otherwise, flag it for regular validity checking.
3. Partition the stochastic_petri_net_model into sub-models based on the flags (preservation or regular validity checking).
4. For each transition in the model:
    - Find corresponding event data in the event_log.
    - If no corresponding event data is found:
        - Combine the transition with its preceding and/or succeeding transitions to create a grouped sub-model.
5. For each sub-model:
    - Validate the sub-model using the validation_policy and discrepancy_threshold.
6. If the validation results exceed the discrepancy_threshold:
    - Start the recalibration process for the sub-model.
7. While recalibration_threshold is not reached:
    - If recalibrated sub-model still exceeds the discrepancy_threshold:
        - Repeat recalibration (go to Step 6).
8. If recalibration_threshold is reached and acceptable results are not found:
    - Re-extract the sub-model and repeat the process.
