import streamlit as st

st.set_page_config(page_title="Lea-testin valitsin", page_icon="📋", layout="wide")

st.title("📋 Lea-testin ammattilaisvalitsin")
st.write("Valitse lapsen ikä ja kehitystaso löytääksesi oikeat testivälineet. Logiikka perustuu Lea-test.fi ohjeistuksiin.")

# --- SIVUPALKKI / KYSYMYKSET ---
st.sidebar.header("Testaustilanne")

ika = st.sidebar.select_slider(
    "Lapsen ikä:",
    options=["0-6 kk", "6-12 kk", "1-2 v", "2.5-3 v", "3-4 v", "4-7 v"]
)

# Dynaaminen etäisyysvalinta: alle 2v vain lähitesti
if ika in ["0-6 kk", "6-12 kk", "1-2 v"]:
    etaisyys = "Lähitesti / Kommunikaatioetäisyys"
    st.sidebar.info("Alle 2-vuotiaille suositellaan vain lähitestausta.")
else:
    etaisyys = st.sidebar.radio("Testausetäisyys:", ["Kaukonäkö (3 m)", "Lähinäkö (40 cm)"])

tapa = st.sidebar.radio(
    "Testaustapa:",
    ["Rivitesti (Standardi)", "Yksittäiset symbolit (Jos rivitesti on liian vaikea / Crowding)"]
)

st.divider()

# --- TUOTEDATA ---
def tuote_kortti(nimi, koodi, kuvaus, linkki_handle):
    url = f"https://leatest.fi/products/{linkki_handle}"
    st.success(f"### {nimi} (Tuotekoodi: #{koodi})")
    st.write(kuvaus)
    st.link_button("Katso tuote kaupassa 🛒", url)

# --- SUOSITUSLOGIIKKA ---
st.subheader(f"Suositeltu testi: {ika} ikäryhmälle")

if ika == "0-6 kk":
    tuote_kortti(
        "Lea Grating Paddles -hila-testi", "253300",
        "Vauvojen näöntarkkuuden mittaamiseen hila-testillä. Seurataan lapsen katselusuunnan kohdistumista raitakuvioon.",
        "goodlite-253300-paddles-lea-gratings-a-preferential-looking-test"
    )
    st.info("💡 **Lisäksi suositellaan:** Hiding Heidi -kontrastitesti (#253500) viestintäetäisyyden arviointiin.")

elif ika == "6-12 kk":
    tuote_kortti(
        "Hiding Heidi -kontrastikasvotesti", "253500",
        "Matalan kontrastin tunnistaminen on tärkeää viestinnän kehityksen kannalta. Auttaa arvioimaan, miltä etäisyydeltä lapsi näkee kasvot.",
        "goodlite-253500-cards-hiding-heidi-low-contrast-face-test-double-sided"
    )

elif ika == "1-2 v":
    tuote_kortti(
        "Lea Symbols -palapeli (3D)", "251600",
        "Ennen varsinaista testausta lapsen on opittava tunnistamaan symbolit. Palapeli on paras tapa tähän kehitysvaiheeseen.",
        "goodlite-251600-good-lite-lea-3d-puzzle-with-symbol-shapes"
    )

elif ika == "2.5-3 v":
    if etaisyys == "Lähinäkö (40 cm)":
        tuote_kortti("Lea Symbols -lähitesti johdolla", "250800", "Standardi lähitesti 40 cm etäisyydelle.", "goodlite-250800-cardnear-lea-symbols-near-vision-card-16-40cm")
    else:
        tuote_kortti("Lea Symbols -kaukonäkötaulu (10 riviä)", "250250", "Pienemmille lapsille soveltuva selkeämpi 10 rivin taulu 3 metrin etäisyydelle.", "goodlite-250250-folding-chart-lea-symbols-distance-vision-screener-10ft-3m")

elif ika in ["3-4 v", "4-7 v"]:
    if tapa == "Yksittäiset symbolit (Jos rivitesti on liian vaikea / Crowding)":
        tuote_kortti(
            "Lea Symbols -yksittäissymbolien testikirja", "250600",
            "Käytetään, jos lapsella on ahtausilmiöstä (crowding) johtuvia vaikeuksia rivitestissä. Sisältää kehystetyt symbolit.",
            "goodlite-250600-flip-book-lea-symbols-single-symbol-book-set-10ft-3m"
        )
    else:
        if ika == "3-4 v":
            tuote_kortti("Lea Symbols -kaukonäkötaulu (10 riviä)", "250250", "Standardi seulonta 3 metrin etäisyydeltä.", "goodlite-250250-folding-chart-lea-symbols-distance-vision-screener-10ft-3m")
        else:
            tuote_kortti("Lea Symbols -kaukonäkötaulu (15 riviä)", "250150", "Tarkempi seulontataulu vanhemmille lapsille 3 metrin etäisyydelle.", "goodlite-250150-folding-chart-lea-symbols-distance-chart-10ft-3m")

st.divider()

# --- NÄÖN KEHITYS 0-7 VUOTTA ---
with st.expander("ℹ️ Lapsen näön kehityksen virstanpylväät (0-7 v.)"):
    st.write("""
    * **0–6 kk:** Preferential looking -menetelmä. Vauva seuraa suurikontrastisia kuvioita.
    * **6–12 kk:** Sosiaalinen hymy ja kasvojen tunnistus matalalla kontrastilla (Hiding Heidi).
    * **1–2 v:** Opitaan symbolien muodot (Ympyrä, neliö, talo, omena) palapelin avulla.
    * **2,5–3 v:** Lähinäön testaaminen onnistuu usein ensin. Kaukoseulonta voidaan aloittaa.
    * **3–4 v:** Kriittinen seulontaikä. Crowding-ilmiö (ahtaus) voi vaikeuttaa rivitestiä.
    * **4–7 v:** Näöntarkkuus lähestyy aikuisten tasoa. Testataan standardiriveillä.
    """)

st.caption("Päivitetty logiikka 2024. Kaikki tuotteet ovat alkuperäisiä Lea-testejä (Good-Lite).")
