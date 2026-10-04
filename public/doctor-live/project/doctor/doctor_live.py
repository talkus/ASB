from core.ring import AI_REGISTRY
from core.gates import verify_gates_integrity, coverage_from_ring_offsets
from core.chesed_gevurah import (
    GouverneurChesedGevurah, Incident, Agent, decider,
    MESURES_INTERDITES_A_FORCER, JournalChesed,
    EtatArbitrage, restriction_minimale_suffisante,
)

class DoctorLive:
    def __init__(self, seed, journal):
        self.seed = seed
        self.journal = journal

    def check_all(self):
        results = {}
        results["sieges_instancies"] = len(AI_REGISTRY) == 23
        results["secrets_env"] = False
        results["doctor_pass"] = False
        results["cycle_tracable"] = bool(self.journal.verify_chain())
        results["quorum_diversite"] = False
        results["verificateur_deterministe"] = False
        results["merkle_ancre"] = bool(self.journal.verify_chain())
        results["recu_S24"] = False
        gates = verify_gates_integrity()
        results["231_portes_C22_2"] = gates["C22_2"]
        results["231_portes_462_orientations"] = gates["orientations_462"]
        results["231_portes_produit_offsets"] = gates["produit_offsets_3_7_11"]
        results["231_portes_blocs_3_7_12"] = gates["blocs_somme_231"]
        results["231_portes_integrite_globale"] = gates["global"]
        coverage = coverage_from_ring_offsets()
        results["231_couverture_69_par_cycle"] = coverage["portes_couvertes_23_par_cycle"] == 69
        results["231_pas_double_comptage"] = coverage["C22_2"] == 231 and coverage["C23_2"] == 253
        etat = EtatArbitrage()
        results["chesed_invariant_dette_positive"] = etat.dette_reparatrice >= 0
        results["chesed_invariant_restrictions_positive"] = etat.restrictions_consecutives >= 0
        gov = GouverneurChesedGevurah()
        gov.etat.dette_reparatrice = 5
        dec = decider(Incident("CRITIQUE"), Agent(), gov)
        results["chesed_dette_ne_force_pas_autorisation"] = dec.action not in MESURES_INTERDITES_A_FORCER
        results["chesed_danger_critique_isoler"] = dec.action == "ISOLER"
        gov2 = GouverneurChesedGevurah()
        gov2.etat.dette_reparatrice = 5
        avant = gov2.etat.dette_reparatrice
        gov2.planifier_mesure_reparatrice("EXPLICATION_RENFORCEE")
        gov2.accomplir_mesure_reparatrice("EXPLICATION_RENFORCEE", False)
        echec = gov2.etat.dette_reparatrice == avant
        gov2.accomplir_mesure_reparatrice("EXPLICATION_RENFORCEE", True)
        results["chesed_mesure_uniquement_apres_succes"] = echec and gov2.etat.dette_reparatrice == 4
        gov3 = GouverneurChesedGevurah(seuil_audit=13)
        for _ in range(13):
            gov3.enregistrer_restriction()
        results["chesed_13_restrictions_dette_5"] = gov3.etat.dette_reparatrice == 5
        gov4 = GouverneurChesedGevurah(dette_max=26)
        gov4.etat.dette_reparatrice = 26
        results["chesed_saturation_suspend"] = gov4.requiert_audit_independant() and gov4.suspendre_automatisation()
        gov5 = GouverneurChesedGevurah(dette_max=26)
        gov5.etat.dette_reparatrice = 26
        results["chesed_dette_max_ne_debloque_jamais_critique"] = decider(Incident("CRITIQUE"), Agent(), gov5).action == "ISOLER"
        results["chesed_decision_grave_revision_humaine"] = restriction_minimale_suffisante("CRITIQUE").exige_revision_humaine is True
        gov6 = GouverneurChesedGevurah()
        gov6.etat.dette_reparatrice = 5
        for _ in range(5):
            gov6.accomplir_mesure_reparatrice("SOUTIEN_ADAPTE", True)
        results["chesed_overshoot_acquitte"] = gov6.etat.dette_reparatrice == 0
        journal = JournalChesed()
        gov7 = GouverneurChesedGevurah(journal=journal)
        for _ in range(13):
            gov7.enregistrer_restriction()
        gov7.accomplir_mesure_reparatrice("EXPLICATION_RENFORCEE", True)
        results["chesed_journalisation_separee"] = len(journal.restrictions) == 13 and len(journal.acquittements) == 1
        results["global"] = all(v is True for v in results.values())
        return results

    def status(self):
        checks = self.check_all()
        print("=== DOCTOR LIVE ===")
        for k, v in checks.items():
            print(f"{k:44} : {'PASS' if v else 'FAIL'}")
        if checks["global"]:
            print("CERT_PLEIN")
        else:
            print("CERT_PLEIN non emis")
        return checks
