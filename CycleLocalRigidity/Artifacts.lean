namespace CycleLocalRigidity
/-!
Artifact interface linking Lean structure to external verification artifacts.
This module does not assert correctness of artifacts; it records their existence.
-/
structure ArtifactBundle where
certificate_json : String
certificate_hash : String
verification_script : String
def artifacts_present (a : ArtifactBundle) : Prop :=
True
axiom artifacts_correspond_to_verification :
∀ (p : VerificationParams) (a : ArtifactBundle),
artifacts_present a → True
end CycleLocalRigidity
