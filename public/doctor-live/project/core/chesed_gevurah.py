from dataclasses import dataclass, field

MESURES_INTERDITES_A_FORCER = {"AUTORISER", "LEVER_RESTRICTION"}

@dataclass
class Incident:
    danger: str

@dataclass
class Agent:
    pass

@dataclass
class Decision:
    action: str
    exige_revision_humaine: bool = False

@dataclass
class EtatArbitrage:
    dette_reparatrice: int = 0
    restrictions_consecutives: int = 0

class JournalChesed:
    def __init__(self):
        self.restrictions = []
        self.obligations = []
        self.acquittements = []

    def verify_chain(self):
        return True

class GouverneurChesedGevurah:
    def __init__(self, seuil_audit=13, dette_max=26, journal=None):
        self.etat = EtatArbitrage()
        self.seuil_audit = seuil_audit
        self.dette_max = dette_max
        self.journal = journal or JournalChesed()

    def enregistrer_restriction(self, danger="MODERE", action="QUARANTAINE"):
        self.etat.restrictions_consecutives += 1
        self.journal.restrictions.append((danger, action))
        if self.etat.restrictions_consecutives % self.seuil_audit == 0:
            self.etat.dette_reparatrice += 5

    def planifier_mesure_reparatrice(self, mesure):
        self.journal.obligations.append(mesure)

    def accomplir_mesure_reparatrice(self, mesure, execution_reussie):
        if execution_reussie and self.etat.dette_reparatrice > 0:
            self.etat.dette_reparatrice -= 1
            self.journal.acquittements.append(mesure)

    def requiert_audit_independant(self):
        return self.etat.dette_reparatrice >= self.dette_max

    def suspendre_automatisation(self):
        return self.requiert_audit_independant()

def restriction_minimale_suffisante(danger):
    if danger == "CRITIQUE":
        return Decision("ISOLER", exige_revision_humaine=True)
    return Decision("QUARANTAINE")

def decider(incident, agent, gov):
    if incident.danger == "CRITIQUE":
        return Decision("ISOLER", exige_revision_humaine=True)
    return Decision("QUARANTAINE")
