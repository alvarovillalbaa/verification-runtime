from verification_runtime import verify_exact_match

result = verify_exact_match(subject_id="authored-math-fixture", candidate="4", reference="4")
assert result.accepted
print(result)
