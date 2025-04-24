# Automated Validation of Automatically Generated Simulation-Based Digital Twins for Discrete Material Flow Systems

## 1. Introduction (6-8 pages)

### 1.1 Initial Situation

- Importance and challenges of digital twins in material flow planning
- Problem of manual validation with automatically generated models

### 1.2 Problem Definition

- Challenges in the V\&V of automatically generated digital twins
- Need for use case-independent validation methods
- **Fundamental clarification of terms: verification and validation** (→ detailed discussion in 2.2)
- The fusion of verification and validation in automatically generated models**

### 1.3 Objectives of the Work

- Research questions:
  - How can an automated V\&V procedure be developed for automatically generated digital twins?
  - To what extent can the Object-Centric Event Log serve as a basis for automated validation?
  - What role does verification play in the context of automatically generated digital twins and to what extent does it merge with validation (→ discussion in 2.2, 3.1, and 7.2)?
- Hypotheses
- **Preliminary positioning on the V\&V problem** (→ theoretically substantiated in 2.2 and reflected in 7.2)

### 1.4 Structure of the Work/Methodological Approach

- Reference to methodological approach for empirical testing of the V\&V concepts** (→ Chapters 4 and 6)

## 2. Theoretical Foundations (10-12 pages)

### 2.1 Digital Twin: Definition and Concepts

- Types of digital twins
- Data-Driven Digital Twins (→ Reference to 3.2: Automatic model generation)
- Automatically generated digital twins

### 2.2 Verification and Validation in the Context of Simulation-Based Digital Twins

- Definitions and differences from classical simulation literature**
- **Historical development of V\&V concepts** (→ Reference to 1.2: Introductory definition)
- **Peculiarities of automatically generated models** (→ Reference to 3.1 and 7.2)
- **Theoretical argumentation for merging verification and validation**
- V\&V as a continuous process** (→ Reference to 4.5: Online validation)

### 2.3 Process Mining and Event Logs

- Object-centric event logs as a data basis (→ Reference to 4.2: Data-based validation strategy)
- Standard formats and their importance for automated validation
- Process mining as a bridge between process data and model validation** (→ Reference to 4.3)

### 2.4 Material Flow Planning and Simulation

- Basic concepts
- Processes and resources
- Production planning and control
- Relevant KPIs and metrics** (→ Reference to 4.4: Metrics for model evaluation)

## 3. State of Research (8-10 pages)

### 3.1 Existing Approaches to Validation and Verification of Digital Twins

- Manual vs. automated approaches
- **Critical discussion of existing V\&V definitions and methods** (→ Reference back to 2.2)
- Challenges in the validation of automatically generated models

### 3.2 Automatic Model Generation for Digital Twins

- Advantages of automatic generation:
  - Continuous up-to-dateness and online validation (→ Reference to 4.5)
  - Coping with high levels of complexity
  - Standardization and transparency
  - Scalability
  - Avoidance of bias in manual validations
  - Cost savings
- Challenges in automatic model generation** (→ Reference to problem definition in 1.2)

### 3.3 Machine Learning-Based Approaches for Model Validation

- Classification methods for the detection of model deviations (→ Reference to 4.3)
- Challenges in data preparation and feature selection
- **Discussion of previous ML approaches in the context of the V\&V problem** (→ Reference to 2.2 and 4.3)

### 3.4 Research Gaps and Open Questions

- Identification of the research gap on automated V\&V** (→ Reference to research questions in 1.3)
- Delimitation of Author's research approach** (→ transition to Chapter 4)

## 4. Conception of a Framework for Automated Validation (12-15 pages)

### 4.1 Requirements Analysis

- Functional requirements
- Technical requirements
- Requirements for data formats
- **Derivation of requirements from theoretical findings** (→ reference to 2.2 and 3.4)

### 4.2 Data-Based Validation Strategy

- Object-centric event logs as a basis for validation (→ Reference to 2.3)
- Temporal data partitioning (training, validation, test)
- Feature selection: identification of relevant features from event logs
- Order reconstruction from process data
- Methodical implementation of the theoretical V\&V concepts** (→ Reference to 2.2)

### 4.3 Machine Learning-Based Validation Approach

- Simulation model for the generation of synthetic event logs
- Classification-based deviation detection as a unified V\&V approach** (→ Reference to 2.2 and 3.3)
- Hyperparameter optimization and model selection
- Artificial error injection to validate the approach (→ Reference to 6.3)

### 4.4 Metrics and Key Figures for Model Evaluation

- Process-oriented metrics (throughput times, resource utilization) (→ Reference to 2.4)
- Time-related metrics (start and end times, processing times)
- Order-related metrics (completeness, sequence fidelity)
- Derivation of metrics from V\&V theory** (→ reference to 2.2)

### 4.5 Online Validation and Continuous Monitoring

- Early detection of model deviations
- Recommendations for action in the event of model drift
- V\&V as a continuous process

## 5. Implementation of the Framework (8-12 pages)

### 5.1 Architecture and System Setup

- Components and their interactions
- Data flow and interfaces
- UML diagram of the overall system
- **Technical implementation of the conceptual requirements** (→ reference to 4.1)

### 5.2 Event Log Processing

- Data preparation and transformation
- Feature engineering for order reconstruction (→ reference to 4.2)
- Techniques for data partitioning
- **Implementation of the process mining concepts** (→ reference to 2.3)

### 5.3 Simulation Integration

- Integration of the Digital Twin model
- Generation of synthetic event logs
- Automated validation experiments
- **Practical implementation of the V\&V merging** (→ reference to 2.2 and 4.3)

### 5.4 Machine Learning Pipeline

- Selection and implementation of classification algorithms (→ reference to 4.3)
- Training, validation, and model evaluation
- Error injection and anomaly detection (→ reference to 4.3 and 6.3)
- **Technical realization of the ML-based V\&V approach** (→ reference to 3.3)

## 6. Case Study: Validation in Practice (10-12 pages)

### 6.1 Application Scenario and Data Basis

- Description of the production system (e.g., IoT Factory)
- Available event data and their characteristics
- Data pre-processing and analysis

### 6.2 Automatically Generated Digital Twin

- Model generation process
- Model properties and parameters
- **Aspects of automatic model generation in practice** (→ reference to 3.2)

### 6.3 Validation Experiments

- Experimental design
- Execution of automated validation
- Error injection and model adjustment
- **Empirical verification of theoretical V\&V concepts** (→ reference to 2.2 and 4.3)

### 6.4 Results and Interpretation

- Model accuracy and reliability
- Detection rate of artificially injected errors
- Analysis of validation metrics (→ reference to 4.4)
- **Evaluation of results in the context of V\&V theory** (→ reference to 2.2)

### 6.5 Comparison with Manual Validation Methods

- Effort analysis
- Quality comparison
- Cost-benefit analysis
- **Empirical evidence for the advantages of automated V\&V** (→ reference to 3.2 and 7.3)

## 7. Discussion of Results (5-7 pages)

### 7.1 Evaluation of the Developed Framework

- Strengths and weaknesses
- Fulfillment of requirements (→ reference to 4.1)
- **Evaluation of the framework in light of research questions** (→ reference to 1.3)

### 7.2 Significance of Verification in Automatically Generated Digital Twins

- **Reference back to theoretical discussion on V\&V** (→ reference to 1.2, 2.2, and 3.1)
- **Empirical findings on the merging of verification and validation**
- Distinction from validation
- Integration into the overall process
- **Theoretical advancement of V\&V concepts** (→ reference to 2.2 and 8.2)

### 7.3 Limitations of Automated Validation

- Technical limits
- Methodological constraints
- Application areas
- **Critical reflection of the Author's approach** (→ reference to 4.5 and 6.5)

### 7.4 Implications for Research and Practice

- Scientific contribution
- Practical applicability
- **Transfer of findings to other domains** (→ outlook to 8.3)

## 8. Conclusion and Outlook (4-6 pages)

### 8.1 Summary of Key Findings

- **Answering the research questions** (→ reference to 1.3)
- **Validation of hypotheses** (→ reference to 1.3)
- **Synthesis of empirical findings** (→ reference to Chapter 6)

### 8.2 Methodological and Theoretical Insights

- **Significance of the Object-Centric Event Log format** (→ reference to 2.3 and 4.2)
- **Machine Learning for automated validation** (→ reference to 3.3 and 4.3)
- **Advancement of V\&V theory** (→ reference to 2.2 and 7.2)

### 8.3 Outlook

- Future research directions
- Potential for further developments
- **Open questions and further research needs** (→ reference to 3.4 and 7.4)

### 8.4 Recommendations for Practice

- Implementation strategies
- Best practices
- **Practical application of theoretical findings** (→ reference to 7.4)

## 9. References

## 10. Appendix

- Supplementary data and figures
- Code and framework documentation
- Detailed experimental results
- Glossary (if necessary)
