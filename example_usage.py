from client import LLMEvalBenchmarkGraderClient
client = LLMEvalBenchmarkGraderClient()
print(client.grade("Output is correct", "Output is correct"))