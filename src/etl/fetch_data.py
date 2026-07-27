import os
from datetime import datetime
from datasets import load_dataset
from src.database.connection import SessionLocal
from src.database.models import Document, Chunk

def fetch_and_store_data(limit=100):
    dataset = load_dataset("AgentPublic/piaf", split="train")
    
    session = SessionLocal()
    
    # On isole les textes (contextes) uniques pour éviter les doublons
    unique_texts = list(set(dataset["context"]))[:limit]
        
    for i, texte in enumerate(unique_texts):
        doc_id = f"DOC_{i+1}"
        
        doc = Document(
            id=doc_id,
            titre=f"Texte encyclopédique n°{i+1}",
            theme="Général / Encyclopédique",
            public_cible="Tout public",
            date_mise_a_jour=datetime.now(),
            url_source="HuggingFace: piaf"
        )
        session.add(doc)

        # Pour l'instant on met tout le texte dans un seul chunk
        chunk = Chunk(
            document_id=doc_id,
            texte=texte,
            position=1,
            nb_tokens=len(texte.split()) 
        )
        session.add(chunk)
    
    session.commit()
    session.close()
    print("Les documents sont dans la base de données locale.")

if __name__ == "__main__":
    fetch_and_store_data(100)
