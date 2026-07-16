# QNA Answer-Writing Rollout Plan

Operational companion to `QNA-INTERVIEW-STANDARD.md` (same root, non-lab-scoped). That file is
the concept-level spec (AMGB structure, QNA-ANSWER-SPEC v1 bullet format). This file is the
plan + status log for turning ~11,000 `parked` questions into `answered` ones across both labs.
Nothing to push for this doc itself — it lives outside any git repo.

**Rebuilt 2026-07-16 09:00 IST (Thursday).** The version of this doc written earlier the same day
used the wrong data source for "foundation" and has been fully replaced. See "Correction" section
below for what was wrong and why.

## Correction — 2026-07-16: the first version of this plan used the wrong foundation grouping

The original plan grouped modules by `contentStatus.js`'s `sourceFile` field (the source-code
file a module's content happens to live in). That is a legacy code-organization artifact, not a
topic taxonomy — it produced groups like `foundationsRunnerData` (16 GSL modules that actually
span at least 4 real, unrelated topics: Language Models, Prompt Engineering, Retrieval, Foundation
Models) and batch-process names like `deepen-thin`, `breadth-2`, `market-gap` that are not
foundations at all. Caught by direct user review before any further batches were written.

**Corrected foundation source, confirmed complete against every module in both labs:**
- **GSL**: `src/data/moduleSearchIndex.js`, field `gymLabel` — 15 real gyms, 131/131 modules
  matched, 0 unmatched.
- **MSL**: `src/data/foundationsModuleIndex.js`, field `domain` (keyed by `moduleId`) — 18 real
  domains represented among modules with QnA content (`FOUNDATION_MODULE_INDEX` defines 20; two,
  Data Foundations aside, all others found live modules), 206/206 modules matched, 0 unmatched.

Everything below uses this corrected grouping. Total roster count is unchanged (337 modules,
11,049 questions total / 333 modules, 10,927 questions remaining `parked`) since it's the same
modules — only the grouping and display names changed.

## Granularity and sequencing (unchanged from original agreement, restated for clarity)

- **Batch = one (tier, foundation, lab) unit.** Every module inside that unit ships together.
- **Sequence: Tier S → A → B.** Within a tier, foundations are ordered GSL-before-MSL, then
  alphabetically by foundation name within each lab. This ordering is a default for determinism,
  not something the user has explicitly ranked by interview-frequency — open to reordering on
  request (e.g. if a specific foundation should jump the queue).
- **Display structure below is Lab → Foundation → Tier** (per the user's explicit ask: "should
  have simply been: lab-foundation-tier, and within it you name all the modules it covers"), which
  is the human-readable roster. The **execution sequence** (which batch gets written next) still
  runs Tier S → A → B across both labs — see "Execution sequence" section — since that was
  separately confirmed and not something the user asked to change.

## Full roster (Lab → Foundation → Tier → modules)

### GSL — 131 modules / 4,257 questions total — 128 modules / 4,166 questions remaining (`parked`)

### GSL / AI Agents

**Tier S** (8 modules):
- `agent-config-lab` — 34q — parked
- `agent-design-challenge` — 33q — parked
- `agent-eval-trajectory` — 33q — parked
- `agent-frameworks` — 34q — parked
- `agent-loop-simulator` — 33q — parked
- `agent-mcp` — 29q — parked
- `agent-react` — 32q — **answered**
- `agent-tool-design` — 29q — **answered**

**Tier A** (9 modules):
- `agent-a2a` — 36q — parked
- `agent-computer-use` — 37q — parked
- `agent-failure-modes` — 36q — parked
- `agent-long-running` — 32q — parked
- `agent-memory-foundations` — 32q — parked
- `agent-memory-libraries` — 32q — parked
- `agent-multiagent` — 28q — parked
- `agent-planning-patterns` — 34q — parked
- `agent-reliability` — 35q — parked

*Subtotal: 17 modules / 559 questions — remaining: 15 modules / 498 questions*

### GSL / AI Safety & Alignment

**Tier S** (1 module): `bias-lab` — 33q — parked

**Tier A** (5 modules): `alignment-techniques` — 33q, `jailbreak-taxonomy` — 36q,
`llm-security-beyond-injection` — 30q, `red-teaming` — 29q, `safety-measurement` — 29q (all parked)

*Subtotal: 6 modules / 190 questions — remaining: 6 modules / 190 questions*

### GSL / Code Generation & AI Coding

**Tier S** (4 modules): `codegen-agentic-loops` — 35q, `codegen-eval-passk-swebench` — 33q,
`codegen-model-training-fim` — 32q, `codegen-repo-context-retrieval` — 32q (all parked)

**Tier A** (1 module): `codegen-security-sandboxing` — 33q — parked

*Subtotal: 5 modules / 165 questions — remaining: 5 modules / 165 questions*

### GSL / Evaluation

**Tier S** (3 modules): `eval-loop` — 31q, `llm-as-judge` — 33q, `rag-eval` — 35q (all parked)

**Tier A** (5 modules): `calibration` — 33q, `debug` — 35q, `eval-contamination` — 35q,
`eval-design` — 34q, `hallucination-lab` — 32q (all parked)

*Subtotal: 8 modules / 268 questions — remaining: 8 modules / 268 questions*

### GSL / Foundation Models

**Tier S** (5 modules): `dpo` — 35q, `finetuning-vs-rag` — 32q, `grpo-rlvr` — 29q, `lora` — 32q,
`rlhf` — 33q (all parked)

**Tier A** (7 modules): `distillation` — 33q, `instruction-tuning` — 31q, `model-families` — 33q,
`moe` — 33q, `pretraining` — 31q, `quantization` — 33q, `scaling-laws` — 32q (all parked)

*Subtotal: 12 modules / 387 questions — remaining: 12 modules / 387 questions*

### GSL / Inference Optimization & Serving

**Tier A** (5 modules): `infra-batching-throughput` — 30q, `infra-edge-ondevice` — 35q,
`infra-paged-attention-kv` — 28q, `infra-prefill-decode` — 31q, `infra-serving-stacks` — 35q
(all parked)

*Subtotal: 5 modules / 159 questions — remaining: 5 modules / 159 questions*

### GSL / Language Models

**Tier S** (9 modules): `attention` — 36q, `gqa-mqa` — 32q, `hallucination` — 30q,
`nextoken` — 31q, `sampling` — 34q, `sparse-attention` — 33q, `tokenizer` — 35q,
`training-signal` — 37q (all parked), `transformer` — 30q — **answered** (grandfathered prose pilot)

**Tier A** (6 modules): `kv-cache` — 28q, `positional-encoding` — 37q, `rope` — 33q,
`seq-parallel` — 31q, `speculative-decoding` — 33q, `tempgame` — 32q (all parked)

*Subtotal: 15 modules / 492 questions — remaining: 14 modules / 462 questions*

### GSL / Model Customization & Fine-Tuning

**Tier A** (5 modules): `custom-data-curation` — 36q, `custom-eval-driven-loop` — 29q,
`custom-peft-lora-serving` — 32q, `custom-preference-alignment` — 29q,
`custom-when-to-finetune` — 29q (all parked)

*Subtotal: 5 modules / 155 questions — remaining: 5 modules / 155 questions*

### GSL / Multimodal AI

**Tier A** (4 modules): `multimodal-rag` — 26q, `ocr-pipeline-design` — 33q,
`resolution-token-cost` — 33q, `vision-language-arch` — 33q (all parked)

*Subtotal: 4 modules / 125 questions — remaining: 4 modules / 125 questions*

### GSL / NLP Foundations

**Tier S** (12 modules): `nlp-bow-tfidf` — 34q, `nlp-classical-tasks` — 34q,
`nlp-encoder-decoder-objectives` — 34q, `nlp-eval-metrics` — 33q, `nlp-ngram-lm` — 32q,
`nlp-preprocessing` — 36q, `nlp-rnn-lstm-gru` — 35q, `nlp-sentence-embeddings` — 37q,
`nlp-seq2seq-attention` — 33q, `nlp-text-classification` — 35q, `nlp-transfer-learning` — 34q,
`nlp-word2vec-glove` — 33q (all parked)

*Subtotal: 12 modules / 410 questions — remaining: 12 modules / 410 questions*

### GSL / Production Systems

**Tier S** (2 modules): `context-budget-lab` — 28q, `cost-latency-concepts` — 29q (all parked)

**Tier A** (11 modules): `cost-attribution` — 26q, `enterprise-ai-cost-model` — 34q,
`failure-sim-lab` — 37q, `flashattn` — 30q, `latency-planner` — 33q,
`managed-vs-selfhosted` — 31q, `model-routing-cascades` — 33q, `observability-concepts` — 32q,
`prompt-regression-signals` — 32q, `quality-drift` — 33q, `streaming-lab` — 30q (all parked)

*Subtotal: 13 modules / 408 questions — remaining: 13 modules / 408 questions*

### GSL / Prompt Engineering

**Tier S** (4 modules): `chain-of-thought` — 30q, `few-shot` — 29q, `prompt-security` — 34q,
`zero-shot` — 31q (all parked)

**Tier A** (6 modules): `injection-lab` — 33q, `multiturn-context` — 33q, `prompt-caching` — 28q,
`prompt-library` — 32q, `structured-outputs` — 32q, `system-prompts` — 31q (all parked)

*Subtotal: 10 modules / 313 questions — remaining: 10 modules / 313 questions*

### GSL / Retrieval

**Tier S** (5 modules): `chunking` — 29q, `dense-vs-sparse-retrieval` — 29q, `embeddings` — 35q,
`rag-pipeline` — 35q, `reranking` — 33q (all parked)

**Tier A** (4 modules): `context` — 36q, `multi-hop-retrieval` — 32q, `query-rewriting` — 30q,
`rag-ingestion-pipeline` — 36q (all parked)

*Subtotal: 9 modules / 295 questions — remaining: 9 modules / 295 questions*

### GSL / Vector Infrastructure

**Tier A** (5 modules): `hybrid-search-design` — 27q, `metadata-filtering` — 31q,
`pgvector-vs-managed` — 32q, `vector-db-index-mechanics` — 33q, `vector-migration-patterns` — 35q
(all parked)

*Subtotal: 5 modules / 158 questions — remaining: 5 modules / 158 questions*

### GSL / Voice & Speech AI

**Tier S** (3 modules): `voice-asr-architectures` — 36q, `voice-realtime-agents` — 34q,
`voice-streaming-latency` — 33q (all parked)

**Tier A** (2 modules): `voice-eval-wer-mos` — 32q, `voice-tts-cloning` — 38q (all parked)

*Subtotal: 5 modules / 173 questions — remaining: 5 modules / 173 questions*

---

### MSL — 206 modules / 6,792 questions total — 205 modules / 6,761 questions remaining (`parked`)

### MSL / Bandits Foundations

**Tier A** (6 modules): `bandits_in_recsys` — 34q, `contextual_bandits` — 35q,
`epsilon_greedy` — 33q, `mab_problem` — 32q, `thompson_sampling` — 33q, `ucb_algorithms` — 35q
(all parked)

**Tier B** (3 modules): `linucb` — 35q, `non_stationary_bandits` — 32q,
`off_policy_evaluation` — 33q (all parked)

*Subtotal: 9 modules / 302 questions — remaining: 9 modules / 302 questions*

### MSL / Causal Foundations

**Tier S** (3 modules): `dag_confounding` — 33q, `pot_outcomes` — 32q, `rct_design` — 33q
(all parked)

**Tier A** (5 modules): `did` — 31q, `iv` — 28q, `observational_ci` — 35q, `rdd` — 31q,
`uplift_modeling` — 36q (all parked)

**Tier B** (2 modules): `mediation` — 33q, `sensitivity_analysis` — 32q (all parked)

*Subtotal: 10 modules / 324 questions — remaining: 10 modules / 324 questions*

### MSL / Classical ML Foundations

**Tier S** (8 modules): `class_imbalance_classical_ml` — 40q, `generalization` — 35q,
`gradient_boosting` — 37q, `linear_regression` — 34q, `logistic_regression` — 31q —
**answered** (grandfathered prose pilot), `random_forest` — 35q, `regularization` — 34q,
`trees` — 34q

**Tier A** (6 modules): `calibration` — 37q, `ensembles` — 35q, `feature_selection` — 40q,
`knn` — 32q, `naive_bayes` — 32q, `svm` — 24q (all parked)

*Subtotal: 14 modules / 480 questions — remaining: 13 modules / 449 questions*

### MSL / Data Foundations

**Tier S** (3 modules): `class_imbalance` — 33q, `data_splits_and_leakage` — 36q,
`feature_engineering` — 34q (all parked)

**Tier A** (7 modules): `categorical_encoding` — 34q, `data_quality_audit` — 37q,
`data_versioning_and_pipelines` — 35q, `distribution_shift` — 32q, `feature_scaling` — 35q,
`feature_selection_data` — 32q, `missing_value_handling` — 33q (all parked)

**Tier B** (1 module): `data_augmentation` — 34q — parked

*Subtotal: 11 modules / 375 questions — remaining: 11 modules / 375 questions*

### MSL / Deep Learning Foundations

**Tier S** (4 modules): `attention` — 33q, `backprop` — 33q, `neural_nets` — 30q,
`transformers` — 33q (all parked)

**Tier A** (5 modules): `activations` — 34q, `batch_norm` — 29q, `cnns` — 34q,
`optimizers` — 34q, `rnns_lstms` — 35q (all parked)

**Tier B** (5 modules): `dl_debugging` — 33q, `dl_serving` — 32q, `finetune` — 35q,
`pretraining` — 35q, `quantization` — 33q (all parked)

*Subtotal: 14 modules / 463 questions — remaining: 14 modules / 463 questions*

### MSL / Evaluation Foundations

**Tier S** (6 modules): `auc_roc` — 34q, `cross_validation` — 35q,
`metrics_first_principles` — 35q, `offline_vs_online` — 35q, `ranking_metrics` — 32q,
`validation_traps` — 37q (all parked)

**Tier A** (5 modules): `ablation` — 35q, `calibration_eval` — 37q, `error_analysis` — 33q,
`evaluation_in_prod` — 33q, `online_experimentation_ml` — 30q (all parked)

*Subtotal: 11 modules / 376 questions — remaining: 11 modules / 376 questions*

### MSL / Graph ML Foundations

**Tier B** (9 modules): `gnn_applications` — 35q, `graph_attention` — 35q,
`graph_representations` — 34q, `heterogeneous_graphs` — 32q, `link_prediction` — 35q,
`message_passing_framework` — 33q, `node_classification_at_scale` — 33q, `spatial_gcn` — 32q,
`spectral_gcn` — 37q (all parked)

*Subtotal: 9 modules / 306 questions — remaining: 9 modules / 306 questions*

### MSL / Math & Stats Foundations

**Tier S** (4 modules): `hypothesis_testing` — 35q, `mle_map` — 31q, `probability_basics` — 32q,
`sampling_distributions` — 33q (all parked)

**Tier A** (8 modules): `convex_optimization` — 32q, `eigendecomposition` — 36q,
`information_theory` — 33q, `joint_distributions` — 32q, `linear_algebra_basics` — 33q,
`pca_theory` — 33q, `random_variables` — 32q, `svd` — 32q (all parked)

**Tier B** (6 modules): `bayesian_inference_mathstats` — 29q, `calculus_ml` — 33q,
`concentration_inequalities` — 33q, `em_algorithm` — 34q, `matrix_calculus` — 31q,
`monte_carlo` — 32q (all parked)

*Subtotal: 18 modules / 586 questions — remaining: 18 modules / 586 questions*

### MSL / Monitoring Foundations

**Tier A** (4 modules): `concept_drift` — 32q, `data_drift_detection` — 36q,
`monitoring_taxonomy` — 33q, `prediction_monitoring` — 33q (all parked)

**Tier B** (4 modules): `alerting_runbooks` — 33q, `calibration_monitoring` — 33q,
`feature_importance_drift` — 36q, `silent_model_staleness` — 37q (all parked)

*Subtotal: 8 modules / 273 questions — remaining: 8 modules / 273 questions*

### MSL / Optimization Foundations

**Tier S** (1 module): `gradient_descent_fundamentals` — 33q — parked

**Tier A** (5 modules): `adagrad_rmsprop` — 34q, `adam_adamw` — 33q,
`learning_rate_schedules` — 33q, `momentum` — 29q, `sgd_and_minibatch` — 35q (all parked)

**Tier B** (6 modules): `gradient_clipping_regularization` — 35q, `gradient_flow` — 33q,
`loss_landscape_geometry` — 32q, `loss_landscape_intuition` — 29q, `second_order_methods` — 33q,
`weight_initialization` — 35q (all parked)

*Subtotal: 12 modules / 394 questions — remaining: 12 modules / 394 questions*

### MSL / Pricing Analytics Foundations

**Tier B** (7 modules): `causal_price_experiments` — 32q, `dynamic_and_surge_pricing` — 33q,
`price_elasticity_of_demand` — 27q, `price_optimization_under_constraints` — 31q,
`promotion_and_discount_uplift` — 31q, `revenue_vs_margin_objective` — 29q,
`willingness_to_pay_and_competition` — 32q (all parked)

*Subtotal: 7 modules / 215 questions — remaining: 7 modules / 215 questions*

### MSL / Probabilistic ML Foundations

**Tier A** (1 module): `calibration_probabilistic` — 33q — parked

**Tier B** (8 modules): `approximate_inference` — 37q, `bayesian_inference` — 38q,
`bayesian_neural_networks` — 34q, `gaussian_processes` — 36q, `information_geometry` — 37q,
`probabilistic_graphical_models` — 32q, `vae_foundations` — 33q, `variational_inference` — 34q
(all parked)

*Subtotal: 9 modules / 314 questions — remaining: 9 modules / 314 questions*

### MSL / Production Foundations

**Tier S** (2 modules): `ab_infra` — 33q, `training_serving_skew` — 32q (all parked)

**Tier A** (9 modules): `data_quality` — 34q, `feature_engineering_prod` — 32q,
`feature_store` — 29q, `feature_store_traps` — 28q, `label_generation` — 30q,
`late_arriving_data` — 33q, `model_registry` — 34q, `online_learning` — 32q, `pipelines` — 32q
(all parked)

*Subtotal: 11 modules / 349 questions — remaining: 11 modules / 349 questions*

### MSL / Recommender Systems Foundations

**Tier S** (6 modules): `candidate_generation` — 33q, `cold_start` — 31q,
`feedback_loops_bias` — 31q, `learning_to_rank` — 29q, `offline_online_eval` — 32q,
`two_stage_architecture` — 32q (all parked)

**Tier A** (4 modules): `features_and_freshness` — 29q, `multi_objective_tradeoffs` — 34q,
`recsys_dl_architectures` — 33q, `recsys_representation_learning` — 28q (all parked)

*Subtotal: 10 modules / 312 questions — remaining: 10 modules / 312 questions*

### MSL / Reinforcement Learning Foundations

**Tier B** (10 modules): `actor_critic` — 30q, `bellman_equations` — 31q,
`deep_q_networks` — 32q, `exploration_exploitation` — 35q, `mdp_framework` — 32q,
`policy_gradients` — 33q, `ppo_trpo` — 36q, `rl_production` — 34q,
`rlhf_reward_modeling` — 33q, `temporal_difference` — 37q (all parked)

*Subtotal: 10 modules / 333 questions — remaining: 10 modules / 333 questions*

### MSL / Self-supervised Foundations

**Tier B** (9 modules): `byol_barlow` — 32q, `clip_alignment` — 33q, `contrastive_loss` — 29q,
`downstream_adaptation` — 32q, `masked_autoencoders` — 31q, `moco` — 33q, `simclr` — 31q,
`ssl_for_tabular` — 32q, `ssl_overview` — 28q (all parked)

*Subtotal: 9 modules / 281 questions — remaining: 9 modules / 281 questions*

### MSL / System Design Foundations

**Tier S** (4 modules): `cold_start_system_design` — 30q, `design_framework` — 31q,
`recsys_overview` — 34q, `recsys_stack` — 30q (all parked)

**Tier A** (10 modules): `embeddings_ann` — 30q, `ml_platform` — 33q, `multitask_ranking` — 33q,
`ranking_systems` — 29q, `real_time_ml` — 36q, `recsys_feedback_loops` — 31q,
`reranking_diversity` — 28q, `semantic_search` — 31q, `sequential_recsys` — 32q,
`two_tower` — 33q (all parked)

**Tier B** (1 module): `ranking_calibration` — 28q — parked

*Subtotal: 15 modules / 469 questions — remaining: 15 modules / 469 questions*

### MSL / Time Series Foundations

**Tier B** (9 modules): `arima_family` — 33q, `causal_ts` — 37q, `exponential_smoothing` — 34q,
`forecast_evaluation` — 33q, `neural_forecasting` — 33q, `prophet_framework` — 34q,
`seasonality_decomposition` — 32q, `stationarity` — 32q, `ts_anomaly_detection` — 37q (all parked)

*Subtotal: 9 modules / 305 questions — remaining: 9 modules / 305 questions*

### MSL / Unsupervised Foundations

**Tier A** (4 modules): `anomaly_detection` — 37q, `clustering_overview` — 34q, `gmm` — 35q,
`kmeans` — 32q (all parked)

**Tier B** (6 modules): `autoencoders_dim_reduction` — 35q, `dbscan` — 32q,
`hierarchical` — 33q, `pca` — 34q, `topic_modeling` — 34q, `tsne_umap` — 29q (all parked)

*Subtotal: 10 modules / 335 questions — remaining: 10 modules / 335 questions*

## Execution sequence (64 batches total, Tier S → A → B, GSL-before-MSL, alphabetical within lab)

### Tier S

1. **GSL / AI Agents / Tier S** — 6 modules remaining, 196 questions: `agent-config-lab`, `agent-design-challenge`, `agent-eval-trajectory`, `agent-frameworks`, `agent-loop-simulator`, `agent-mcp`
2. **GSL / AI Safety & Alignment / Tier S** — 1 module, 33 questions: `bias-lab`
3. **GSL / Code Generation & AI Coding / Tier S** — 4 modules, 132 questions: `codegen-agentic-loops`, `codegen-eval-passk-swebench`, `codegen-model-training-fim`, `codegen-repo-context-retrieval`
4. **GSL / Evaluation / Tier S** — 3 modules, 99 questions: `eval-loop`, `llm-as-judge`, `rag-eval`
5. **GSL / Foundation Models / Tier S** — 5 modules, 161 questions: `dpo`, `finetuning-vs-rag`, `grpo-rlvr`, `lora`, `rlhf`
6. **GSL / Language Models / Tier S** — 8 modules, 268 questions: `attention`, `gqa-mqa`, `hallucination`, `nextoken`, `sampling`, `sparse-attention`, `tokenizer`, `training-signal`
7. **GSL / NLP Foundations / Tier S** — 12 modules, 410 questions: `nlp-bow-tfidf`, `nlp-classical-tasks`, `nlp-encoder-decoder-objectives`, `nlp-eval-metrics`, `nlp-ngram-lm`, `nlp-preprocessing`, `nlp-rnn-lstm-gru`, `nlp-sentence-embeddings`, `nlp-seq2seq-attention`, `nlp-text-classification`, `nlp-transfer-learning`, `nlp-word2vec-glove`
8. **GSL / Production Systems / Tier S** — 2 modules, 57 questions: `context-budget-lab`, `cost-latency-concepts`
9. **GSL / Prompt Engineering / Tier S** — 4 modules, 124 questions: `chain-of-thought`, `few-shot`, `prompt-security`, `zero-shot`
10. **GSL / Retrieval / Tier S** — 5 modules, 161 questions: `chunking`, `dense-vs-sparse-retrieval`, `embeddings`, `rag-pipeline`, `reranking`
11. **GSL / Voice & Speech AI / Tier S** — 3 modules, 103 questions: `voice-asr-architectures`, `voice-realtime-agents`, `voice-streaming-latency` **← next batch**
12. **MSL / Causal Foundations / Tier S** — 3 modules, 98 questions: `dag_confounding`, `pot_outcomes`, `rct_design`
13. **MSL / Classical ML Foundations / Tier S** — 7 modules, 249 questions: `class_imbalance_classical_ml`, `generalization`, `gradient_boosting`, `linear_regression`, `random_forest`, `regularization`, `trees`
14. **MSL / Data Foundations / Tier S** — 3 modules, 103 questions: `class_imbalance`, `data_splits_and_leakage`, `feature_engineering`
15. **MSL / Deep Learning Foundations / Tier S** — 4 modules, 129 questions: `attention`, `backprop`, `neural_nets`, `transformers`
16. **MSL / Evaluation Foundations / Tier S** — 6 modules, 208 questions: `auc_roc`, `cross_validation`, `metrics_first_principles`, `offline_vs_online`, `ranking_metrics`, `validation_traps`
17. **MSL / Math & Stats Foundations / Tier S** — 4 modules, 131 questions: `hypothesis_testing`, `mle_map`, `probability_basics`, `sampling_distributions`
18. **MSL / Optimization Foundations / Tier S** — 1 module, 33 questions: `gradient_descent_fundamentals`
19. **MSL / Production Foundations / Tier S** — 2 modules, 65 questions: `ab_infra`, `training_serving_skew`
20. **MSL / Recommender Systems Foundations / Tier S** — 6 modules, 188 questions: `candidate_generation`, `cold_start`, `feedback_loops_bias`, `learning_to_rank`, `offline_online_eval`, `two_stage_architecture`
21. **MSL / System Design Foundations / Tier S** — 4 modules, 125 questions: `cold_start_system_design`, `design_framework`, `recsys_overview`, `recsys_stack`

### Tier A

22. **GSL / AI Agents / Tier A** — 9 modules, 302 questions: `agent-a2a`, `agent-computer-use`, `agent-failure-modes`, `agent-long-running`, `agent-memory-foundations`, `agent-memory-libraries`, `agent-multiagent`, `agent-planning-patterns`, `agent-reliability`
23. **GSL / AI Safety & Alignment / Tier A** — 5 modules, 157 questions: `alignment-techniques`, `jailbreak-taxonomy`, `llm-security-beyond-injection`, `red-teaming`, `safety-measurement`
24. **GSL / Code Generation & AI Coding / Tier A** — 1 module, 33 questions: `codegen-security-sandboxing`
25. **GSL / Evaluation / Tier A** — 5 modules, 169 questions: `calibration`, `debug`, `eval-contamination`, `eval-design`, `hallucination-lab`
26. **GSL / Foundation Models / Tier A** — 7 modules, 226 questions: `distillation`, `instruction-tuning`, `model-families`, `moe`, `pretraining`, `quantization`, `scaling-laws`
27. **GSL / Inference Optimization & Serving / Tier A** — 5 modules, 159 questions: `infra-batching-throughput`, `infra-edge-ondevice`, `infra-paged-attention-kv`, `infra-prefill-decode`, `infra-serving-stacks`
28. **GSL / Language Models / Tier A** — 6 modules, 194 questions: `kv-cache`, `positional-encoding`, `rope`, `seq-parallel`, `speculative-decoding`, `tempgame`
29. **GSL / Model Customization & Fine-Tuning / Tier A** — 5 modules, 155 questions: `custom-data-curation`, `custom-eval-driven-loop`, `custom-peft-lora-serving`, `custom-preference-alignment`, `custom-when-to-finetune`
30. **GSL / Multimodal AI / Tier A** — 4 modules, 125 questions: `multimodal-rag`, `ocr-pipeline-design`, `resolution-token-cost`, `vision-language-arch`
31. **GSL / Production Systems / Tier A** — 11 modules, 351 questions: `cost-attribution`, `enterprise-ai-cost-model`, `failure-sim-lab`, `flashattn`, `latency-planner`, `managed-vs-selfhosted`, `model-routing-cascades`, `observability-concepts`, `prompt-regression-signals`, `quality-drift`, `streaming-lab`
32. **GSL / Prompt Engineering / Tier A** — 6 modules, 189 questions: `injection-lab`, `multiturn-context`, `prompt-caching`, `prompt-library`, `structured-outputs`, `system-prompts`
33. **GSL / Retrieval / Tier A** — 4 modules, 134 questions: `context`, `multi-hop-retrieval`, `query-rewriting`, `rag-ingestion-pipeline`
34. **GSL / Vector Infrastructure / Tier A** — 5 modules, 158 questions: `hybrid-search-design`, `metadata-filtering`, `pgvector-vs-managed`, `vector-db-index-mechanics`, `vector-migration-patterns`
35. **GSL / Voice & Speech AI / Tier A** — 2 modules, 70 questions: `voice-eval-wer-mos`, `voice-tts-cloning`
36. **MSL / Bandits Foundations / Tier A** — 6 modules, 202 questions: `bandits_in_recsys`, `contextual_bandits`, `epsilon_greedy`, `mab_problem`, `thompson_sampling`, `ucb_algorithms`
37. **MSL / Causal Foundations / Tier A** — 5 modules, 161 questions: `did`, `iv`, `observational_ci`, `rdd`, `uplift_modeling`
38. **MSL / Classical ML Foundations / Tier A** — 6 modules, 200 questions: `calibration`, `ensembles`, `feature_selection`, `knn`, `naive_bayes`, `svm`
39. **MSL / Data Foundations / Tier A** — 7 modules, 238 questions: `categorical_encoding`, `data_quality_audit`, `data_versioning_and_pipelines`, `distribution_shift`, `feature_scaling`, `feature_selection_data`, `missing_value_handling`
40. **MSL / Deep Learning Foundations / Tier A** — 5 modules, 166 questions: `activations`, `batch_norm`, `cnns`, `optimizers`, `rnns_lstms`
41. **MSL / Evaluation Foundations / Tier A** — 5 modules, 168 questions: `ablation`, `calibration_eval`, `error_analysis`, `evaluation_in_prod`, `online_experimentation_ml`
42. **MSL / Math & Stats Foundations / Tier A** — 8 modules, 263 questions: `convex_optimization`, `eigendecomposition`, `information_theory`, `joint_distributions`, `linear_algebra_basics`, `pca_theory`, `random_variables`, `svd`
43. **MSL / Monitoring Foundations / Tier A** — 4 modules, 134 questions: `concept_drift`, `data_drift_detection`, `monitoring_taxonomy`, `prediction_monitoring`
44. **MSL / Optimization Foundations / Tier A** — 5 modules, 164 questions: `adagrad_rmsprop`, `adam_adamw`, `learning_rate_schedules`, `momentum`, `sgd_and_minibatch`
45. **MSL / Probabilistic ML Foundations / Tier A** — 1 module, 33 questions: `calibration_probabilistic`
46. **MSL / Production Foundations / Tier A** — 9 modules, 284 questions: `data_quality`, `feature_engineering_prod`, `feature_store`, `feature_store_traps`, `label_generation`, `late_arriving_data`, `model_registry`, `online_learning`, `pipelines`
47. **MSL / Recommender Systems Foundations / Tier A** — 4 modules, 124 questions: `features_and_freshness`, `multi_objective_tradeoffs`, `recsys_dl_architectures`, `recsys_representation_learning`
48. **MSL / System Design Foundations / Tier A** — 10 modules, 316 questions: `embeddings_ann`, `ml_platform`, `multitask_ranking`, `ranking_systems`, `real_time_ml`, `recsys_feedback_loops`, `reranking_diversity`, `semantic_search`, `sequential_recsys`, `two_tower`
49. **MSL / Unsupervised Foundations / Tier A** — 4 modules, 138 questions: `anomaly_detection`, `clustering_overview`, `gmm`, `kmeans`

### Tier B

50. **MSL / Bandits Foundations / Tier B** — 3 modules, 100 questions: `linucb`, `non_stationary_bandits`, `off_policy_evaluation`
51. **MSL / Causal Foundations / Tier B** — 2 modules, 65 questions: `mediation`, `sensitivity_analysis`
52. **MSL / Data Foundations / Tier B** — 1 module, 34 questions: `data_augmentation`
53. **MSL / Deep Learning Foundations / Tier B** — 5 modules, 168 questions: `dl_debugging`, `dl_serving`, `finetune`, `pretraining`, `quantization`
54. **MSL / Graph ML Foundations / Tier B** — 9 modules, 306 questions: `gnn_applications`, `graph_attention`, `graph_representations`, `heterogeneous_graphs`, `link_prediction`, `message_passing_framework`, `node_classification_at_scale`, `spatial_gcn`, `spectral_gcn`
55. **MSL / Math & Stats Foundations / Tier B** — 6 modules, 192 questions: `bayesian_inference_mathstats`, `calculus_ml`, `concentration_inequalities`, `em_algorithm`, `matrix_calculus`, `monte_carlo`
56. **MSL / Monitoring Foundations / Tier B** — 4 modules, 139 questions: `alerting_runbooks`, `calibration_monitoring`, `feature_importance_drift`, `silent_model_staleness`
57. **MSL / Optimization Foundations / Tier B** — 6 modules, 197 questions: `gradient_clipping_regularization`, `gradient_flow`, `loss_landscape_geometry`, `loss_landscape_intuition`, `second_order_methods`, `weight_initialization`
58. **MSL / Pricing Analytics Foundations / Tier B** — 7 modules, 215 questions: `causal_price_experiments`, `dynamic_and_surge_pricing`, `price_elasticity_of_demand`, `price_optimization_under_constraints`, `promotion_and_discount_uplift`, `revenue_vs_margin_objective`, `willingness_to_pay_and_competition`
59. **MSL / Probabilistic ML Foundations / Tier B** — 8 modules, 281 questions: `approximate_inference`, `bayesian_inference`, `bayesian_neural_networks`, `gaussian_processes`, `information_geometry`, `probabilistic_graphical_models`, `vae_foundations`, `variational_inference`
60. **MSL / Reinforcement Learning Foundations / Tier B** — 10 modules, 333 questions: `actor_critic`, `bellman_equations`, `deep_q_networks`, `exploration_exploitation`, `mdp_framework`, `policy_gradients`, `ppo_trpo`, `rl_production`, `rlhf_reward_modeling`, `temporal_difference`
61. **MSL / Self-supervised Foundations / Tier B** — 9 modules, 281 questions: `byol_barlow`, `clip_alignment`, `contrastive_loss`, `downstream_adaptation`, `masked_autoencoders`, `moco`, `simclr`, `ssl_for_tabular`, `ssl_overview`
62. **MSL / System Design Foundations / Tier B** — 1 module, 28 questions: `ranking_calibration`
63. **MSL / Time Series Foundations / Tier B** — 9 modules, 305 questions: `arima_family`, `causal_ts`, `exponential_smoothing`, `forecast_evaluation`, `neural_forecasting`, `prophet_framework`, `seasonality_decomposition`, `stationarity`, `ts_anomaly_detection`
64. **MSL / Unsupervised Foundations / Tier B** — 6 modules, 197 questions: `autoencoders_dim_reduction`, `dbscan`, `hierarchical`, `pca`, `topic_modeling`, `tsne_umap`

## Progress log

### 2026-07-16 08:40 IST — Batch 1 written: GSL / AI Agents / Tier S (partial)

Written before the foundation-grouping correction, under the wrong `agent-core` sourceFile unit:
`agent-react` (32q) + `agent-tool-design` (29q) = 61 questions, both flipped to `answered`.

**Correction to this entry**: under the real (tier, foundation, lab) unit — GSL / AI Agents /
Tier S — the batch has **8 modules total, not 2**. The 61 questions written are genuinely done and
correct (spec-compliant, verified, applied) — nothing here needs rework. But the batch itself is
only **2/8 modules complete**. Remaining 6: `agent-config-lab` (34q), `agent-design-challenge`
(33q), `agent-eval-trajectory` (33q), `agent-frameworks` (34q), `agent-loop-simulator` (33q),
`agent-mcp` (29q) — 196 questions.

**Next batch = finishing GSL / AI Agents / Tier S** (the remaining 6 modules above), before moving
to sequence item 2 (GSL / AI Safety & Alignment / Tier S). This keeps batch 1 whole under the
corrected granularity rather than leaving it permanently half-done.


### 2026-07-16 09:59 IST — GSL / AI Agents / Tier S closed out (6 remaining modules)

`agent-config-lab` (34q), `agent-design-challenge` (33q), `agent-eval-trajectory` (33q),
`agent-frameworks` (34q), `agent-loop-simulator` (33q), `agent-mcp` (29q) — 196 questions, all
flipped to `answered`. Drafted by 6 parallel writer agents (one per module), grounded strictly in
each module's own source content, no new facts introduced. Independently re-validated
programmatically against the full spec checklist across all 196 questions — 0 real violations (one
flagged item was a documented spec exception: Mechanism bullet count == N when Answer names N
parallel components). Applied via the centralized single-writer script. Full detail in GSL's
`docs/GSL_PLAN.md` 2026-07-16 09:59 IST entry.

**Sequence item 1 (GSL / AI Agents / Tier S) is now closed: 8/8 modules, 257 questions, all
`answered`.** Next batch: sequence item 2, GSL / AI Safety & Alignment / Tier S (1 module,
`bias-lab`, 33 questions).


### 2026-07-16 11:06 IST — GSL / Code Generation & AI Coding / Tier S done (sequence item 3)

`codegen-agentic-loops` (35q), `codegen-eval-passk-swebench` (33q), `codegen-model-training-fim`
(32q), `codegen-repo-context-retrieval` (32q) — 132 questions, all flipped to `answered`. 4
parallel writer agents, one per module. Independently re-validated programmatically across all 132
questions — 0 violations. Also fixed two QnAPanel display bugs this round (bullet-array rendering,
category-label display) — see GSL's `docs/GSL_PLAN.md` 2026-07-16 11:06 IST entry for detail.

**Sequence items 1–3 are now closed: 13 modules, 361 questions, all `answered`.** Next batch:
sequence item 4, GSL / Evaluation / Tier S (3 modules: `eval-loop`, `llm-as-judge`, `rag-eval`, 99
questions).


### 2026-07-16 12:25 IST — GSL / Evaluation / Tier S done (sequence item 4); L0-L3/S-A-B hover tooltips added (both labs)

`eval-loop` (31q), `rag-eval` (35q), `llm-as-judge` (33q) — 99 questions, all flipped to
`answered`. 3 parallel writer agents, one per module. Independently re-validated programmatically
across all 99 questions — 2 minor Boundary-bullet-count gaps found in `llm-as-judge` (enumerative
"what are the other biases" style questions), hand-patched with source-grounded bullets, 0
violations on re-check. `eval-loop`'s full narrative content turned out to live in
`src/data/foundationsRunnerData.js` rather than `src/data/foundations/recap-patch-a.js` (which
only carries its `keyPoints`/`recap`) — caught by grepping for named examples several questions
reference directly ("the Friday-grading example", "The Twelve Questions") before drafting, so no
answer was written from thin/wrong grounding.

Also shipped, per explicit user request, before this batch: hover tooltips on the L0-L3 level
filter chips (real definitions from `QNA-INTERVIEW-STANDARD.md`'s level taxonomy) and on the
"Build S/A/B tier tracks" button (real S/A/B semantics from `moduleTiers.js`), across both GSL
(`src/components/QnAPanel.jsx`, `src/MyTracks.jsx`) and MSL
(`src/components/foundations/QnAPanel.jsx`, `src/tabs/MyTracksTab.jsx`) — see GSL's
`docs/GSL_PLAN.md` 2026-07-16 12:25 IST entry for full detail.

**Sequence items 1–4 are now closed: 16 modules, 460 questions, all `answered`.** Next batch:
sequence item 5, GSL / Foundation Models / Tier S (5 modules: `dpo`, `finetuning-vs-rag`,
`grpo-rlvr`, `lora`, `rlhf`, 161 questions).


### 2026-07-16 13:15 IST — GSL / Foundation Models / Tier S done (sequence item 5)

`dpo` (35q), `finetuning-vs-rag` (32q), `grpo-rlvr` (29q), `lora` (32q), `rlhf` (33q) — 161
questions, all flipped to `answered`. 5 parallel writer agents, one per module. Independently
re-validated programmatically across all 161 questions — 6 flagged in `lora` (Grounding-bullet
count one over the level band, each citing a genuinely distinct real number), reviewed by hand and
accepted as legitimate content-driven exceptions, 0 fabricated facts. See GSL's `docs/GSL_PLAN.md`
2026-07-16 13:15 IST entry for full detail.

**Sequence items 1–5 are now closed: 21 modules, 621 questions, all `answered`.** Next batch:
sequence item 6, GSL / Language Models / Tier S (8 modules: `attention`, `gqa-mqa`,
`hallucination`, `nextoken`, `sampling`, `sparse-attention`, `tokenizer`, `training-signal`, 268
questions).


### 2026-07-16 14:10 IST — GSL / Language Models / Tier S done (sequence item 6); time-estimate badges archived (both labs)

`attention` (36q), `gqa-mqa` (32q), `hallucination` (30q), `nextoken` (31q), `sampling` (34q),
`sparse-attention` (33q), `tokenizer` (35q), `training-signal` (37q) — 268 questions, all flipped
to `answered`. 8 parallel writer agents, one per module. Independently re-validated
programmatically across all 268 questions — 1 flagged in `gqa-mqa` (0 Grounding bullets on an L0
question), hand-patched with a real named example (Llama-2-70B's GQA-8, PaLM/Falcon's MQA), 0
issues on re-check.

Also shipped, per explicit user request, before this batch: time-estimate badges ("X min") removed
from render across both labs — MSL's 19 foundation tabs (sidebar + header badges) and GSL's
`Concepts.jsx` module grid fallback badge. Data fields left in place, just unused. See GSL's
`docs/GSL_PLAN.md` 2026-07-16 14:10 IST entry for full detail.

**Sequence items 1–6 are now closed: 29 modules, 889 questions, all `answered`.** Next batch:
sequence item 7, GSL / NLP Foundations / Tier S (12 modules: `nlp-bow-tfidf`,
`nlp-classical-tasks`, `nlp-encoder-decoder-objectives`, `nlp-eval-metrics`, `nlp-ngram-lm`,
`nlp-preprocessing`, `nlp-rnn-lstm-gru`, `nlp-sentence-embeddings`, `nlp-seq2seq-attention`,
`nlp-text-classification`, `nlp-transfer-learning`, `nlp-word2vec-glove`, 410 questions).


### 2026-07-16 15:05 IST — GSL / NLP Foundations / Tier S done (sequence item 7, largest batch yet)

12 modules, 410 questions, all flipped to `answered`. 12 parallel writer agents, one per module.
Independently re-validated programmatically across all 410 questions — 10 flagged (Grounding or
Boundary count one over the level band), reviewed by hand and accepted as legitimate
content-driven exceptions (each extra bullet cites a genuinely distinct real fact), 0 fabricated
facts. One writer agent flagged a shared-scratch-file collision in `/tmp/batch8` from concurrent
agents — did not corrupt the deliverable (confirmed via the apply step's 410/410 count check), but
noted as a process risk for future large fan-outs. See GSL's `docs/GSL_PLAN.md` 2026-07-16 15:05
IST entry for full detail.

**Sequence items 1–7 are now closed: 41 modules, 1,299 questions, all `answered`.** Next batch:
sequence item 8, GSL / Production Systems / Tier S (2 modules: `context-budget-lab`,
`cost-latency-concepts`, 57 questions).

### 2026-07-16 15:50 IST (Thursday) — Sequence item 8 closed

GSL / Production Systems / Tier S: `context-budget-lab` (28q) and `cost-latency-concepts` (29q),
57 questions total. AMGB answers written by 2 parallel writer agents, one per module, grounded
strictly in each module's own source content (`src/data/playground/playground-labs.js` and
`src/data/foundations/production-tone.js`) -- no new facts introduced. Independently re-validated
programmatically against the full spec checklist -- 0 flagged, clean on first pass (no hand-patch
or exceptions needed, unlike batches 5-8). Applied via centralized single-writer script,
`node --check` clean, 0 duplicate keys across 4,257 total question ids, all 57 confirmed non-empty,
`validate-qna-status.mjs` passes clean.

**Sequence items 1–8 are now closed: 42 modules, 1,356 questions, all `answered`.** Next batch:
sequence item 9, GSL / Prompt Engineering / Tier S (4 modules: `chain-of-thought`, `few-shot`,
`prompt-security`, `zero-shot`, 124 questions).

### 2026-07-16 16:35 IST (Thursday) — Sequence item 9 closed

GSL / Prompt Engineering / Tier S: `zero-shot` (31q), `few-shot` (29q), `chain-of-thought` (30q),
`prompt-security` (34q), 124 questions total. AMGB answers written by 4 parallel writer agents, one
per module, grounded strictly in each module's own source content (`src/data/foundationsRunnerData.js`,
lines 1350-2761) -- no new facts introduced. Independently re-validated programmatically against
the full spec checklist -- 0 flagged, clean on first pass. Applied via centralized single-writer
script, `node --check` clean, 0 duplicate keys across 4,257 total question ids, all 124 confirmed
non-empty, `validate-qna-status.mjs` passes clean.

**Sequence items 1–9 are now closed: 46 modules, 1,480 questions, all `answered`.** Next batch:
sequence item 10, GSL / Retrieval / Tier S (5 modules: `chunking`, `dense-vs-sparse-retrieval`,
`embeddings`, `rag-pipeline`, `reranking`, 161 questions).

### 2026-07-16 17:20 IST (Thursday) — Sequence item 10 closed

GSL / Retrieval / Tier S: `chunking` (29q), `dense-vs-sparse-retrieval` (29q), `embeddings` (35q),
`rag-pipeline` (35q), `reranking` (33q), 161 questions total. AMGB answers written by 5 parallel
writer agents, one per module, grounded strictly in each module's own source content
(`src/data/foundationsRunnerData.js`, `src/data/foundations/retrieval-breadth.js`,
`src/data/foundations/deepen-thin.js`) -- no new facts introduced. Independently re-validated
programmatically against the full spec checklist -- 0 flagged, clean on first pass. Applied via
centralized single-writer script, `node --check` clean, 0 duplicate keys across 4,257 total
question ids, all 161 confirmed non-empty, `validate-qna-status.mjs` passes clean.

**Sequence items 1–10 are now closed: 51 modules, 1,641 questions, all `answered`.** Next batch:
sequence item 11, GSL / Voice & Speech AI / Tier S (3 modules: `voice-asr-architectures`,
`voice-realtime-agents`, `voice-streaming-latency`, 103 questions). This closes out ALL of GSL
Tier S.

## Not yet done

- Sequence items 1–10 (GSL / AI Agents, AI Safety & Alignment, Code Generation & AI Coding,
  Evaluation, Foundation Models, Language Models, NLP Foundations, Production Systems, Prompt
  Engineering, Retrieval, all Tier S) — done, closed (see Progress log).
- Sequence items 11–64 (see Execution sequence above) — all `parked`, not started.
- `logistic_regression` (MSL) and `transformer` (GSL) remain grandfathered prose pilots, not
  reformatted to bullets — see `QNA-INTERVIEW-STANDARD.md` Supersession section.
- This batch's `qnaBank.js`/`qnaStatus.js` changes are not committed/pushed in
  `genai-systems-lab` yet — local working tree only, pending the user running the git commands.

## 2026-07-16 (Thursday) — STRATEGY CHANGE: switched priority source from contentStatus.js to moduleTiers.js

User flagged that "GSL / Voice & Speech AI / Tier S" (originally sequence item 11) didn't match their
expectation of what's Tier S. Investigation found **two distinct "Tier S" concepts** in this codebase:

1. `src/data/moduleTiers.js` `TIER_S` / `TIER_A` — the REAL, live-site-facing S/A/B tier that powers the
   tier badges and tooltips users actually see (25 modules total in GSL's TIER_S: "always asked").
2. `src/data/contentStatus.js`'s per-module `tier` field — a SEPARATE, broader content-audit-priority
   tagging used (unintentionally) as the source for this rollout plan's "Tier S" batch groupings. This is
   why voice-asr-architectures/voice-realtime-agents/voice-streaming-latency were sequenced as "Tier S"
   even though they aren't in moduleTiers.js's TIER_S or TIER_A at all (they render as Tier B on the site).

Cross-checked all 25 modules in the REAL moduleTiers.js TIER_S against what's answered so far: **all 25
are already done** (tokenizer, attention, transformer, sampling, hallucination, embeddings, chunking,
rag-pipeline, reranking, dense-vs-sparse-retrieval, eval-loop, rag-eval, llm-as-judge, zero-shot,
few-shot, chain-of-thought, prompt-security, rlhf, dpo, lora, finetuning-vs-rag, agent-react,
agent-tool-design, agent-eval-trajectory, cost-latency-concepts). The real, most-important, always-asked
S-tier content is 100% answered.

**Decision (user-approved):** switch the rollout's priority source to `moduleTiers.js`'s `TIER_A` array
next (the real "shows up often" tier, ~56 modules), sequenced by the domain-group order the file itself
uses. The remaining contentStatus.js "Tier S" items (voice-*, and anything else from the old sequence
list not yet done) are deprioritized — picked up later, not before real Tier A.

New sequence (moduleTiers.js TIER_A, by domain group as listed in the file):
1. Language Models — `positional-encoding`, `rope`, `speculative-decoding`, `tempgame`, `kv-cache` (5 modules, 163 questions) -- CLOSED 2026-07-16 18:10 IST

### 2026-07-16 18:10 IST (Thursday) -- Tier A group 1 closed

positional-encoding (37q), rope (33q), speculative-decoding (33q), tempgame (32q), kv-cache (28q),
163 questions total. AMGB answers written by 5 parallel writer agents, one per module, grounded
strictly in each module's own source content -- no new facts introduced. Independently re-validated
-- 2 flagged in kv-cache (legitimate Grounding-band exceptions), 0 fabricated facts. Applied via
centralized single-writer script, node --check clean, 0 duplicate keys, all 163 confirmed non-empty,
validate-qna-status.mjs passes clean.

**Cumulative total: 56 modules, 1,804 questions, all `answered`** (all of real Tier S + Tier A group 1).
2. Retrieval — `context`, `query-rewriting`, `multi-hop-retrieval`, `rag-ingestion-pipeline` (4 modules) -- CLOSED 2026-07-16 19:00 IST

### 2026-07-16 19:00 IST (Thursday) -- Tier A group 2 closed

context (36q), query-rewriting (30q), multi-hop-retrieval (32q), rag-ingestion-pipeline (36q),
134 questions total. AMGB answers written by 4 parallel writer agents, one per module, grounded
strictly in each module's own source content -- no new facts introduced. Independently
re-validated -- 2 flagged: 1 real gap hand-patched (context L0 question missing a required
Grounding bullet), 1 accepted as a legitimate Boundary-band exception. Applied via centralized
single-writer script, node --check clean, 0 duplicate keys, all 134 confirmed non-empty,
validate-qna-status.mjs passes clean.

**Cumulative total: 60 modules, 1,938 questions, all `answered`.**
3. Foundation Models — `pretraining`, `instruction-tuning`, `model-families`, `scaling-laws`, `quantization`, `moe`, `distillation` (7 modules) -- CLOSED 2026-07-16 20:00 IST

### 2026-07-16 20:00 IST (Thursday) -- Tier A group 3 closed

pretraining (31q), instruction-tuning (31q), model-families (33q), scaling-laws (32q),
quantization (33q), moe (33q), distillation (33q), 226 questions total -- the largest Tier A batch
so far. AMGB answers written by 7 parallel writer agents, one per module, grounded strictly in each
module's own source content -- no new facts introduced. Independently re-validated -- 0 flagged,
clean on first pass. Applied via centralized single-writer script, node --check clean, 0 duplicate
keys, all 226 confirmed non-empty, validate-qna-status.mjs passes clean.

**Cumulative total: 67 modules, 2,164 questions, all `answered`.**
4. Prompt Engineering — `system-prompts`, `structured-outputs`, `prompt-caching`, `multiturn-context`, `injection-lab` (5 modules) -- CLOSED 2026-07-16 21:00 IST

### 2026-07-16 21:00 IST (Thursday) -- Tier A group 4 closed

system-prompts (31q), structured-outputs (32q), prompt-caching (28q), multiturn-context (33q),
injection-lab (33q), 157 questions total. AMGB answers written by 5 parallel writer agents, one per
module, grounded strictly in each module's own source content -- no new facts introduced.
Independently re-validated -- 2 flagged: 1 under-band case (structured-outputs L2, source has no
numeric confidence threshold) fixed with a second genuinely distinct Grounding bullet, 1 real gap
hand-patched (prompt-caching L0 question missing its required Grounding bullet, fixed with the
module's own 6,050-to-50-token worked-example numbers), 0 fabricated facts. Applied via centralized
single-writer script, node --check clean, 0 duplicate keys, all 157 confirmed non-empty.

**Cumulative total: 72 modules, 2,321 questions, all `answered`.**
5. Vector Infrastructure — `vector-db-index-mechanics`, `hybrid-search-design`, `metadata-filtering`, `pgvector-vs-managed` (4 modules) -- CLOSED 2026-07-16 22:00 IST

### 2026-07-16 22:00 IST (Thursday) -- Tier A group 5 closed

vector-db-index-mechanics (33q), hybrid-search-design (27q), metadata-filtering (31q),
pgvector-vs-managed (32q), 123 questions total. AMGB answers written by 4 parallel writer agents,
one per module, grounded strictly in each module's own source content -- no new facts introduced.
Independently re-validated -- 2 flagged: 1 real over-band count hand-fixed (hybrid-search-design L0,
consolidated to 4 bullets), 1 accepted as a legitimate thin-content exception per spec's explicit
below-band allowance (pgvector-vs-managed L2, all sub-band minimums satisfied). 0 fabricated facts.
Applied via centralized single-writer script, node --check clean, 0 duplicate keys, all 123
confirmed non-empty.

**Cumulative total: 76 modules, 2,444 questions, all `answered`.**
6. AI Agents — `agent-memory-foundations`, `agent-multiagent`, `agent-failure-modes`, `agent-planning-patterns`, `agent-reliability` (5 modules) -- CLOSED 2026-07-16 23:00 IST

### 2026-07-16 23:00 IST (Thursday) -- Tier A group 6 closed

agent-memory-foundations (32q), agent-multiagent (28q), agent-failure-modes (36q),
agent-planning-patterns (34q), agent-reliability (35q), 165 questions total. AMGB answers written
by 5 parallel writer agents, one per module, grounded strictly in each module's own source content
-- no new facts introduced. Independently re-validated -- 3 flagged, all accepted as legitimate
spec-sanctioned exceptions (the "N parallel components -> N Mechanism bullets" rule, applied to
agent-multiagent's two "three patterns"/"three conditions" L0 questions and agent-reliability's
five-pattern L3 question). 0 fabricated facts, 0 hand-patches needed. Applied via centralized
single-writer script, node --check clean, 0 duplicate keys, all 165 confirmed non-empty.

**Cumulative total: 81 modules, 2,609 questions, all `answered`.**
7. Evaluation — `eval-design`, `debug`, `hallucination-lab`, `eval-contamination`, `calibration` (5 modules) -- CLOSED 2026-07-16 23:45 IST

### 2026-07-16 23:45 IST (Thursday) -- Tier A group 7 closed

eval-design (34q), debug (35q), hallucination-lab (32q), eval-contamination (35q), calibration
(33q), 169 questions total. AMGB answers written by 5 parallel writer agents, one per module,
grounded strictly in each module's own source content -- no new facts introduced. Independently
re-validated -- 1 flagged, accepted as a legitimate spec-sanctioned exception (the "N parallel
components -> N Mechanism bullets" rule, hallucination-lab's 3-signature-type L0 question). 0
fabricated facts, 0 hand-patches needed. Applied via centralized single-writer script, node --check
clean, 0 duplicate keys, all 169 confirmed non-empty.

**Cumulative total: 86 modules, 2,778 questions, all `answered`.**
8. Production — `flashattn`, `latency-planner`, `observability-concepts`, `prompt-regression-signals`, `quality-drift`, `cost-attribution`, `managed-vs-selfhosted`, `streaming-lab`, `failure-sim-lab`, `model-routing-cascades` (10 modules) -- CLOSED 2026-07-17 00:30 IST

### 2026-07-17 00:30 IST (Friday) -- Tier A group 8 closed (largest batch)

flashattn (30q), latency-planner (33q), observability-concepts (32q), prompt-regression-signals
(32q), quality-drift (33q), cost-attribution (26q), managed-vs-selfhosted (31q), streaming-lab
(30q), failure-sim-lab (37q), model-routing-cascades (33q), 317 questions total -- the largest
single batch of the rollout. AMGB answers written by 10 parallel writer agents, one per module,
grounded strictly in each module's own source content -- no new facts introduced. Each writer used
a uniquely-named scratch validator (avoiding the prior batch's shared-filename collision) and
self-fixed its own issues before returning. Independently re-validated -- 0 flags, clean on first
pass. 0 fabricated facts. Applied via centralized single-writer script, node --check clean, 0
duplicate keys, all 317 confirmed non-empty.

**Cumulative total: 96 modules, 3,095 questions, all `answered`.**
9. Inference Optimization & Serving — `infra-prefill-decode`, `infra-batching-throughput`, `infra-paged-attention-kv`, `infra-serving-stacks` (4 modules) -- CLOSED 2026-07-17 01:15 IST

### 2026-07-17 01:15 IST (Friday) -- Tier A group 9 closed

infra-prefill-decode (31q), infra-batching-throughput (30q), infra-paged-attention-kv (28q),
infra-serving-stacks (35q), 124 questions total. AMGB answers written by 4 parallel writer agents,
one per module, grounded strictly in each module's own source content -- no new facts introduced.
Independently re-validated -- 1 flagged, accepted as a legitimate spec-sanctioned exception (the
"N parallel components -> N Mechanism bullets" rule, infra-paged-attention-kv's 3-lever L0
question). 0 fabricated facts, 0 hand-patches needed. Applied via centralized single-writer script,
node --check clean, 0 duplicate keys, all 124 confirmed non-empty.

**Cumulative total: 100 modules, 3,219 questions, all `answered`.**
10. Model Customization & Fine-Tuning — `custom-when-to-finetune`, `custom-data-curation`, `custom-peft-lora-serving`, `custom-preference-alignment`, `custom-eval-driven-loop` (5 modules) -- CLOSED 2026-07-17 02:00 IST

### 2026-07-17 02:00 IST (Friday) -- Tier A group 10 closed

custom-when-to-finetune (29q), custom-data-curation (36q), custom-peft-lora-serving (32q),
custom-preference-alignment (29q), custom-eval-driven-loop (29q), 155 questions total. AMGB
answers written by 5 parallel writer agents, one per module, grounded strictly in each module's own
source content -- no new facts introduced. Independently re-validated -- 5 flagged, all accepted as
legitimate spec-sanctioned exceptions (4 under the "N parallel components -> N Mechanism bullets"
rule, 1 under the explicit thin-content allowance for custom-preference-alignment's IPO/KTO
question). 0 fabricated facts, 0 hand-patches needed. Applied via centralized single-writer script,
node --check clean, 0 duplicate keys, all 155 confirmed non-empty.

**Cumulative total: 105 modules, 3,374 questions, all `answered`.**
11. AI Safety & Alignment — `alignment-techniques`, `llm-security-beyond-injection` (2 modules) -- CLOSED 2026-07-17 02:30 IST (FINAL TIER_A GROUP)

### 2026-07-17 02:30 IST (Friday) -- Tier A group 11 closed -- ALL 11 TIER_A GROUPS COMPLETE

alignment-techniques (33q), llm-security-beyond-injection (30q), 63 questions total. AMGB answers
written by 2 parallel writer agents, one per module, grounded strictly in each module's own source
content -- no new facts introduced. Independently re-validated -- 3 flagged, all accepted as
legitimate spec-sanctioned exceptions (the "N parallel components -> N Mechanism bullets" rule,
llm-security-beyond-injection's three 3-component L0 questions: pipe boundaries, exfiltration
flavors, compliance concerns). 0 fabricated facts, 0 hand-patches needed. Applied via centralized
single-writer script, node --check clean, 0 duplicate keys, all 63 confirmed non-empty.

**Cumulative total: 107 modules, 3,437 questions, all `answered`.**

**MILESTONE: real moduleTiers.js Tier S (25 modules) + Tier A (~56 modules, 11 domain groups) are
now 100% complete.** Every module the live site badges as S-tier or A-tier -- the ones that
actually show up as "always asked" or "shows up often" to users -- has a full AMGB answer set.
Remaining ~22 parked GSL modules are Tier B (moduleTiers.js) or leftover contentStatus.js-tagged
items (Voice & Speech AI, etc.) that were never in the real TIER_S/TIER_A. Per the standing
strategy-change plan, these are lower priority and are the next candidates if/when the rollout
resumes.

After real Tier A closes: pick up leftover contentStatus.js "Tier S" items (Voice & Speech AI, etc.),
then moduleTiers.js's implicit Tier B (everything else), then the MSL rollout.

### 2026-07-16 IST (Thursday) -- Tier B closeout batch 1 of 4 closed (Agents & Codegen)
Real Tier S + Tier A are 100% complete (per the 2026-07-17 milestone note above). This begins the closeout of
the remaining 22 GSL modules outside moduleTiers.js real Tier S/A ("Tier B" per user framing), split into 4
sub-batches (23-26). Batch 23 closed: agent-a2a, agent-computer-use, agent-long-running, agent-memory-libraries,
codegen-security-sandboxing -- 170 questions, 0 real gaps found on independent validation (5 flags, all legitimate
spec-sanctioned exceptions). GSL cumulative: 114/131 modules answered, 17 parked.
Remaining queued: batch 24 (Safety/Security/Cost, 6 modules, 192q), batch 25 (Multimodal/Infra/Vector/Prompt,
6 modules, 194q), batch 26 (Voice AI, 5 modules, 173q).

### 2026-07-16 IST (Thursday) -- Tier B closeout batch 2 of 4 closed (Safety, Security & Cost)
Batch 24 closed: enterprise-ai-cost-model, jailbreak-taxonomy, red-teaming, resolution-token-cost,
seq-parallel, safety-measurement -- 192 questions, 0 real gaps found on independent validation (1 flag,
legitimate spec-sanctioned exception). GSL cumulative: 120/131 modules answered, 11 parked.
Remaining queued: batch 25 (Multimodal/Infra/Vector/Prompt, 6 modules, 194q), batch 26 (Voice AI, 5
modules, 173q).

### 2026-07-16 IST (Thursday) -- Tier B closeout batch 3 of 4 closed (Multimodal, Infra, Vector & Prompt)
Batch 25 closed: multimodal-rag, ocr-pipeline-design, vision-language-arch, vector-migration-patterns,
infra-edge-ondevice, prompt-library -- 194 questions, 0 real gaps found on independent validation (3 flags,
all legitimate spec-sanctioned exceptions). GSL cumulative: 126/131 modules answered, 5 parked.
Remaining queued: batch 26 (Voice AI, 5 modules, 173q) -- the FINAL batch, closing GSL to 131/131.

### 2026-07-16 IST (Thursday) -- GSL QnA ANSWER-WRITING ROLLOUT: COMPLETE
Batch 26 (Voice AI, 5 modules, 173 questions) closed -- the fourth and final Tier B closeout sub-batch, and
the final batch of the entire rollout. 0 real gaps found on independent validation (4 flags, all legitimate
spec-sanctioned exceptions).

**Final GSL state: 131/131 modules answered, 0 parked, 0 draft, 4,257 total questions.** Verified directly
against the live qnaBank.js/qnaStatus.js via a full-repo sweep (not just this batch's scope): every module
status is "answered", every question and case across all 131 modules has a non-empty AMGB answer array,
node --check clean on both data files, 0 duplicate keys.

**Rollout summary (26 batches total):**
- Batches 1-14 (prior sessions, before this plan doc's batch-15 starting point): earlier Tier S coverage
  and ad hoc work (including the NLP Foundations domain, 12 modules / 410 questions, completed outside the
  main batch sequence).
- Batches 15-22: completed all 11 real moduleTiers.js TIER_A domain groups (Language Models, Retrieval,
  Foundation Models, Prompt Engineering, Vector Infrastructure, AI Agents, Evaluation, Production, Inference
  Optimization & Serving, Model Customization & Fine-Tuning, AI Safety & Alignment) -- 1,273 questions.
  This closed real Tier S + Tier A entirely (flagged as a milestone at the time).
- Batches 23-26 ("Tier B" closeout, 4 sub-batches): closed all 22 remaining parked modules outside real
  Tier S/A -- Agents & Codegen (170q), Safety/Security/Cost (192q), Multimodal/Infra/Vector/Prompt (194q),
  Voice AI (173q) -- 729 questions total.

Every batch used the same pipeline: parallel per-module writer agents grounded strictly in that module's
own source content, independent re-validation via a fresh Python script per batch against the full
QNA-ANSWER-SPEC v1 checklist, hand-review of every flag to classify as a real gap (hand-patched) vs. a
legitimate spec-sanctioned exception (accepted as-is), centralized apply + status-update scripts, and
node --check + duplicate-key verification before every commit.

**GSL work is done. Attention now shifts to MSL (ml-systems-lab)**, which runs its own separate QnA
answer-writing rollout (own qnaBank.js/qnaStatus.js) and is at a much earlier stage: 1/206 modules answered
(just the logistic_regression pilot module). MSL's curriculum (math/stats, classical ML, eval, unsupervised,
causal inference, production foundations) has no overlap with GSL's real Tier S/A/B tiering system and will
need its own tier/batch plan defined before rollout begins.

---

## MSL (ml-systems-lab) QnA answer-writing rollout — plan established 2026-07-16

GSL's rollout (above) is complete. Starting MSL's now, same pipeline, same QNA-ANSWER-SPEC v1 (AMGB
atomic-bullet format) per QNA-INTERVIEW-STANDARD.md's 2026-07-16 08:40 IST supersession -- no format
changes needed, MSL uses the exact same spec.

**Starting state (2026-07-16):** MSL qnaStatus.js -- 206 total modules, 205 parked, 1 answered
(`logistic_regression`, the original flowing-prose pilot, grandfathered -- not touched by this rollout).
MSL moduleTiers.js -- real Tier S: 40 modules (39 parked + logistic_regression), Tier A: 80 modules (all
parked), Tier B (default, everything else): 86 modules (all parked). Every one of MSL's 206 modules is
`clean` in contentStatus.js (verified via a direct query) -- no eligibility blockers, unlike GSL's earlier
worry about the `clean` gate; MSL's audit pipeline ran ahead of this rollout starting.
Total questions: Tier S 1,327 (1,296 parked + 31 answered), Tier A 2,624, Tier B 2,841 -- 6,792 total across
MSL, vs GSL's 4,257. MSL organizes source content into 23 domain-family files under
`src/data/foundations/*.js` (e.g. `classicalMLModules.js`, `evalModules.js`, `recsysModules.js`), each
module's exact source file given by `contentStatus.js`'s own `sourceFile` field -- more directly queryable
than GSL's source-file guessing.

**Strategy:** same as GSL -- follow real Tier S then Tier A then Tier B (not contentStatus.js's broader
tags), batched by source-family file (mirrors GSL's domain-group batching). Batch numbering continues
from GSL's sequence (GSL ended at batch 26).

**Tier S plan (39 parked modules, 1,296 questions, 6 batches):**
- Batch 27: Classical ML -- class_imbalance_classical_ml, generalization, gradient_boosting,
  linear_regression, random_forest, regularization, trees (7 modules, 249q,
  src/data/foundations/classicalMLModules.js)
- Batch 28: Evaluation -- auc_roc, cross_validation, metrics_first_principles, offline_vs_online,
  ranking_metrics, validation_traps (6 modules, 208q, src/data/foundations/evalModules.js)
- Batch 29: Recommender Systems -- candidate_generation, cold_start, feedback_loops_bias,
  learning_to_rank, offline_online_eval, two_stage_architecture (6 modules, 188q,
  src/data/foundations/recsysModules.js)
- Batch 30: System Design + Production -- cold_start_system_design, design_framework, recsys_overview,
  recsys_stack, ab_infra, training_serving_skew (6 modules, 190q,
  src/data/foundations/systemDesignModules.js + productionModules.js)
- Batch 31: Math & Stats + Causal -- hypothesis_testing, mle_map, probability_basics,
  sampling_distributions, pot_outcomes, rct_design (6 modules, 196q,
  src/data/foundations/mathStatsModules.js + causalModules.js)
- Batch 32: Deep Learning + Optimization + Data -- attention, backprop, neural_nets, transformers,
  gradient_descent_fundamentals, class_imbalance, data_splits_and_leakage, feature_engineering
  (8 modules, 265q, src/data/foundations/deepLearningModules.js + optimizationModules.js + dataModules.js)

**Tier A (80 modules, 2,624 questions) and Tier B (86 modules, 2,841 questions) plans** will be drafted
in the same domain-grouped style once Tier S closes, mirroring GSL's approach of only planning the next
tier once the current one is in flight.

MSL's own narrative-log doc for batch entries is `docs/BACKLOG.md` (its GSL_PLAN.md equivalent) -- each
MSL batch gets a dated entry there, same as GSL's `docs/GSL_PLAN.md` entries.

### 2026-07-16 IST (Thursday) -- MSL batch 27 closed (Classical ML, Tier S batch 1 of 6)
class_imbalance_classical_ml, generalization, gradient_boosting, linear_regression, random_forest,
regularization, trees -- 249 questions, 0 real gaps found on independent validation (7 flags, all
legitimate spec-sanctioned exceptions). Hit and fixed one MSL-specific process quirk: qnaBank.js question
objects with trailing followUp/trap fields need a different apply regex than GSL's (full detail in
docs/BACKLOG.md's 2026-07-16 entry) -- corrected regex now standard for all future MSL batches.
MSL cumulative: 8/206 modules answered, 198 parked.
Remaining Tier S queued: batch 28 (Evaluation, 6 modules, 208q), batch 29 (Recommender Systems, 6 modules,
188q), batch 30 (System Design + Production, 6 modules, 190q), batch 31 (Math & Stats + Causal, 6 modules,
196q), batch 32 (Deep Learning + Optimization + Data, 8 modules, 265q).

### 2026-07-16 IST (Thursday) -- MSL batch 28 closed (Evaluation, Tier S batch 2 of 6)
auc_roc, cross_validation, metrics_first_principles, offline_vs_online, ranking_metrics, validation_traps
-- 208 questions, 0 real gaps found on independent validation (9 flags, all legitimate thin-content
exceptions). Batch 27's apply-script fix applied cleanly from the start this batch -- no second pass
needed. MSL cumulative: 14/206 modules answered, 192 parked.
Remaining Tier S queued: batch 29 (Recommender Systems, 6 modules, 188q), batch 30 (System Design +
Production, 6 modules, 190q), batch 31 (Math & Stats + Causal, 6 modules, 196q), batch 32 (Deep Learning +
Optimization + Data, 8 modules, 265q).

### 2026-07-16 IST (Thursday) -- MSL batch 29 closed (Recommender Systems, Tier S batch 3 of 6)
candidate_generation, cold_start, feedback_loops_bias, learning_to_rank, offline_online_eval,
two_stage_architecture -- 188 questions, 0 real gaps found on independent validation (2 flags, both
legitimate thin-content exceptions). MSL cumulative: 20/206 modules answered, 186 parked.
Remaining Tier S queued: batch 30 (System Design + Production, 6 modules, 190q), batch 31 (Math & Stats +
Causal, 6 modules, 196q), batch 32 (Deep Learning + Optimization + Data, 8 modules, 265q).

### 2026-07-16 IST (Thursday) -- MSL batch 30 closed (System Design + Production, Tier S batch 4 of 6)
cold_start_system_design, design_framework, recsys_overview, recsys_stack, ab_infra,
training_serving_skew -- 190 questions, 1 real hand-patch on independent validation (banned hedge opener
"it depends" in a Boundary bullet, rewritten), 1 legitimate spec-sanctioned exception. MSL cumulative:
26/206 modules answered, 180 parked.
Remaining Tier S queued: batch 31 (Math & Stats + Causal, 6 modules, 196q), batch 32 (Deep Learning +
Optimization + Data, 8 modules, 265q).

### 2026-07-16 IST (Thursday) -- MSL batch 31 closed (Math & Stats + Causal, Tier S batch 5 of 6)
hypothesis_testing, mle_map, probability_basics, sampling_distributions, pot_outcomes, rct_design -- 196
questions, 0 real gaps found on independent validation (2 flags, both legitimate spec-sanctioned
exceptions). MSL cumulative: 32/206 modules answered, 174 parked.
Remaining Tier S queued: batch 32 (Deep Learning + Optimization + Data, 8 modules, 265q) -- final Tier S
batch.

### 2026-07-16 IST (Thursday) -- MSL batch 32 closed (Deep Learning + Optimization + Data, Tier S batch 6 of 6) -- MSL TIER S COMPLETE
attention, backprop, neural_nets, transformers, gradient_descent_fundamentals, class_imbalance,
data_splits_and_leakage, feature_engineering -- 265 questions, 2 real hand-patches on independent
validation (over-count Mechanism bullet trimmed; one Grounding bullet over the 30-word cap trimmed), 3
legitimate spec-sanctioned exceptions. MSL cumulative: 40/206 modules answered, 166 parked.

**MSL Tier S rollout complete: 40/40 Tier S modules answered (batches 27-32, 1,296 questions total),
verified directly against moduleTiers.js's TIER_S array.** Next: MSL Tier A (80 modules, ~2,624 questions)
-- batch plan to be drafted next session, mirroring GSL's tier-by-tier approach.

## MSL Tier A QnA answer-writing rollout — plan established 2026-07-16

Starting state: Tier S fully closed (40/40). Tier A = 80 modules, 2,624 questions, verified against
moduleTiers.js's TIER_A array directly. All 80 confirmed `clean` in contentStatus.js and `parked` in
qnaBank.js -- fully eligible, no blockers. Same QNA-ANSWER-SPEC v1 AMGB format, same pipeline (parallel
writer agents grounded strictly in each module's own source content, independent validator script,
centralized apply script, full-repo verification) used for GSL and MSL Tier S.

Batch plan (12 batches, domain/source-family grouped, following real tier order):

- Batch 33: Classical ML Extended -- ensembles, svm, knn, naive_bayes, calibration, feature_selection
  (200q, 6 modules, classicalMLModules.js)
- Batch 34: Evaluation & Calibration -- calibration_eval, error_analysis, ablation, evaluation_in_prod,
  online_experimentation_ml, calibration_probabilistic (201q, 6 modules, evalModules.js +
  probabilisticMLModules.js)
- Batch 35: Data Quality & Preparation -- feature_selection_data, data_quality_audit,
  missing_value_handling, categorical_encoding, feature_scaling, distribution_shift,
  data_versioning_and_pipelines (238q, 7 modules, dataModules.js)
- Batch 36: Math, Linear Algebra & Convex Optimization Theory -- random_variables, joint_distributions,
  information_theory, linear_algebra_basics, eigendecomposition, svd, pca_theory, convex_optimization
  (263q, 8 modules, mathStatsModules.js)
- Batch 37: Causal Inference -- dag_confounding, observational_ci, iv, did, rdd, uplift_modeling
  (194q, 6 modules, causalModules.js)
- Batch 38: Deep Learning Components -- activations, batch_norm, optimizers, cnns, rnns_lstms
  (166q, 5 modules, deepLearningModules.js)
- Batch 39: Recsys DL & Architecture -- features_and_freshness, multi_objective_tradeoffs,
  recsys_dl_architectures, recsys_representation_learning, two_tower, semantic_search
  (188q, 6 modules, recsysModules.js + systemDesignModules.js partial)
- Batch 40: Recsys Systems & Serving -- multitask_ranking, ml_platform, ranking_systems, real_time_ml,
  sequential_recsys, embeddings_ann, reranking_diversity, recsys_feedback_loops
  (252q, 8 modules, systemDesignModules.js remainder)
- Batch 41: Production Feature & Pipeline Infra -- feature_engineering_prod, feature_store,
  feature_store_traps, late_arriving_data, data_quality, label_generation, pipelines, model_registry,
  online_learning (284q, 9 modules, productionModules.js)
- Batch 42: Monitoring & Unsupervised Learning -- monitoring_taxonomy, data_drift_detection,
  concept_drift, prediction_monitoring, clustering_overview, kmeans, gmm, anomaly_detection
  (272q, 8 modules, monitoringModules.js + unsupervisedModules.js)
- Batch 43: Optimization Algorithms -- sgd_and_minibatch, momentum, adagrad_rmsprop, adam_adamw,
  learning_rate_schedules (164q, 5 modules, optimizationModules.js)
- Batch 44: Multi-Armed & Contextual Bandits -- mab_problem, epsilon_greedy, ucb_algorithms,
  thompson_sampling, contextual_bandits, bandits_in_recsys (202q, 6 modules, banditsModules.js)

Total: 12 batches, 80 modules, 2,624 questions -- matches Tier A's true total exactly.

### 2026-07-16 IST (Thursday) -- MSL batch 33 closed (Classical ML Extended, Tier A batch 1 of 12)
ensembles, svm, knn, naive_bayes, calibration, feature_selection -- 200 questions, 2 real hand-patches on
independent validation (missing Grounding bullet on 2 L0 answers, one sub-15-word Boundary bullet), 3
legitimate spec-sanctioned exceptions. MSL cumulative: 46/206 modules answered, 160 parked.
Remaining Tier A queued: batch 34 (Evaluation & Calibration, 6 modules, 201q), batch 35 (Data Quality &
Preparation, 7 modules, 238q), batch 36 (Math/Linear Algebra/Convex Opt, 8 modules, 263q), batch 37
(Causal Inference, 6 modules, 194q), batch 38 (Deep Learning Components, 5 modules, 166q), batch 39
(Recsys DL & Architecture, 6 modules, 188q), batch 40 (Recsys Systems & Serving, 8 modules, 252q), batch
41 (Production Feature & Pipeline Infra, 9 modules, 284q), batch 42 (Monitoring & Unsupervised Learning, 8
modules, 272q), batch 43 (Optimization Algorithms, 5 modules, 164q), batch 44 (Multi-Armed & Contextual
Bandits, 6 modules, 202q).

### 2026-07-16 IST (Thursday) -- MSL batch 34 closed (Evaluation & Calibration, Tier A batch 2 of 12)
calibration_eval, error_analysis, ablation, evaluation_in_prod, online_experimentation_ml,
calibration_probabilistic -- 201 questions, 1 real hand-patch on independent validation (banned "So"
filler opener rewritten), 4 legitimate spec-sanctioned exceptions. MSL cumulative: 52/206 modules
answered, 154 parked.
Remaining Tier A queued: batch 35 (Data Quality & Preparation, 7 modules, 238q), batch 36
(Math/Linear Algebra/Convex Opt, 8 modules, 263q), batch 37 (Causal Inference, 6 modules, 194q), batch 38
(Deep Learning Components, 5 modules, 166q), batch 39 (Recsys DL & Architecture, 6 modules, 188q), batch
40 (Recsys Systems & Serving, 8 modules, 252q), batch 41 (Production Feature & Pipeline Infra, 9 modules,
284q), batch 42 (Monitoring & Unsupervised Learning, 8 modules, 272q), batch 43 (Optimization Algorithms,
5 modules, 164q), batch 44 (Multi-Armed & Contextual Bandits, 6 modules, 202q).

### 2026-07-16 IST (Thursday) -- MSL batch 35 closed (Data Quality & Preparation, Tier A batch 3 of 12)
feature_selection_data, data_quality_audit, missing_value_handling, categorical_encoding,
feature_scaling, distribution_shift, data_versioning_and_pipelines -- 238 questions, 0 real gaps found on
independent validation (7 flags, all legitimate spec-sanctioned exceptions). MSL cumulative: 59/206
modules answered, 147 parked.
Remaining Tier A queued: batch 36 (Math/Linear Algebra/Convex Opt, 8 modules, 263q), batch 37 (Causal
Inference, 6 modules, 194q), batch 38 (Deep Learning Components, 5 modules, 166q), batch 39 (Recsys DL &
Architecture, 6 modules, 188q), batch 40 (Recsys Systems & Serving, 8 modules, 252q), batch 41 (Production
Feature & Pipeline Infra, 9 modules, 284q), batch 42 (Monitoring & Unsupervised Learning, 8 modules,
272q), batch 43 (Optimization Algorithms, 5 modules, 164q), batch 44 (Multi-Armed & Contextual Bandits, 6
modules, 202q).

### 2026-07-16 IST (Thursday) -- MSL batch 36 closed (Math, Linear Algebra & Convex Optimization Theory, Tier A batch 4 of 12)
random_variables, joint_distributions, information_theory, linear_algebra_basics, eigendecomposition,
svd, pca_theory, convex_optimization -- 263 questions, 4 real hand-patches on independent validation
(three over-30-word Answer bullets trimmed, one over-count Grounding bullet removed), 3 legitimate
spec-sanctioned exceptions. MSL cumulative: 67/206 modules answered, 139 parked.
Remaining Tier A queued: batch 37 (Causal Inference, 6 modules, 194q), batch 38 (Deep Learning
Components, 5 modules, 166q), batch 39 (Recsys DL & Architecture, 6 modules, 188q), batch 40 (Recsys
Systems & Serving, 8 modules, 252q), batch 41 (Production Feature & Pipeline Infra, 9 modules, 284q),
batch 42 (Monitoring & Unsupervised Learning, 8 modules, 272q), batch 43 (Optimization Algorithms, 5
modules, 164q), batch 44 (Multi-Armed & Contextual Bandits, 6 modules, 202q).

### 2026-07-16 IST (Thursday) -- MSL batch 37 closed (Causal Inference, Tier A batch 5 of 12)
dag_confounding, observational_ci, iv, did, rdd, uplift_modeling -- 194 questions, 1 real hand-patch on
independent validation (over-count Mechanism bullets merged), 1 legitimate spec-sanctioned exception. MSL
cumulative: 73/206 modules answered, 133 parked.
Remaining Tier A queued: batch 38 (Deep Learning Components, 5 modules, 166q), batch 39 (Recsys DL &
Architecture, 6 modules, 188q), batch 40 (Recsys Systems & Serving, 8 modules, 252q), batch 41 (Production
Feature & Pipeline Infra, 9 modules, 284q), batch 42 (Monitoring & Unsupervised Learning, 8 modules,
272q), batch 43 (Optimization Algorithms, 5 modules, 164q), batch 44 (Multi-Armed & Contextual Bandits, 6
modules, 202q).

### 2026-07-16 IST (Thursday) -- MSL batch 38 closed (Deep Learning Components, Tier A batch 6 of 12)
activations, batch_norm, optimizers, cnns, rnns_lstms -- 166 questions, 0 real gaps found on independent
validation (1 flag, legitimate spec-sanctioned exception). MSL cumulative: 78/206 modules answered, 128
parked.
Remaining Tier A queued: batch 39 (Recsys DL & Architecture, 6 modules, 188q), batch 40 (Recsys Systems &
Serving, 8 modules, 252q), batch 41 (Production Feature & Pipeline Infra, 9 modules, 284q), batch 42
(Monitoring & Unsupervised Learning, 8 modules, 272q), batch 43 (Optimization Algorithms, 5 modules,
164q), batch 44 (Multi-Armed & Contextual Bandits, 6 modules, 202q).


### 2026-07-16 IST (Thursday) -- MSL batch 39 closed (Recsys DL & Architecture, Tier A batch 7 of 12)
features_and_freshness, multi_objective_tradeoffs, recsys_dl_architectures, recsys_representation_learning,
two_tower, semantic_search -- 188 questions, 0 flags on independent validation, a fully clean first-pass
batch (0 real gaps, 0 hand-patches). MSL cumulative: 84/206 modules answered, 122 parked.
Remaining Tier A queued: batch 40 (Recsys Systems & Serving, 8 modules, 252q), batch 41 (Production
Feature & Pipeline Infra, 9 modules, 284q), batch 42 (Monitoring & Unsupervised Learning, 8 modules,
272q), batch 43 (Optimization Algorithms, 5 modules, 164q), batch 44 (Multi-Armed & Contextual Bandits, 6
modules, 202q).


### 2026-07-16 IST (Thursday) -- MSL batch 40 closed (Recsys Systems & Serving, Tier A batch 8 of 12)
multitask_ranking, ml_platform, ranking_systems, real_time_ml, sequential_recsys, embeddings_ann,
reranking_diversity, recsys_feedback_loops -- 252 questions, 0 flags on independent validation, a fully
clean first-pass batch (0 real gaps, 0 hand-patches). MSL cumulative: 92/206 modules answered, 114
parked.
Remaining Tier A queued: batch 41 (Production Feature & Pipeline Infra, 9 modules, 284q), batch 42
(Monitoring & Unsupervised Learning, 8 modules, 272q), batch 43 (Optimization Algorithms, 5 modules,
164q), batch 44 (Multi-Armed & Contextual Bandits, 6 modules, 202q).
