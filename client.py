class LLMEvalBenchmarkGraderClient:
    def grade(self, output_text: str, ground_truth: str) -> dict:
        return {"factuality_score": 0.95}