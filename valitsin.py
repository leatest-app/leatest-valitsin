import streamlit as st

st.set_page_config(page_title="Lea-testin valitsin", page_icon="📋", layout="wide")

st.title("📋 Lea-testin ammattilaisvalitsin")
st.write("Tämä työkalu auttaa valitsemaan oikean testivälineen lapsen iän ja kehitystason mukaan.")

# --- SIVUPALKKI / KYSYMYKSET ---
st.sidebar.header("Asiakkaan tiedot")

ika = st.sidebar.select_slider(
    "Lapsen ikä:",
    options=["0-6 kk", "6-12 kk", "1-2 v", "3-4 v", "5-7 v"]
)

tapa = st.sidebar.radio(
    "Testaustapa:",
    ["Vakio (Rivitesti)", "Yksittäiset symbolit (Jos rivi on liian vaikea)"]
)

etaisyys = st.sidebar.selectbox(
    "Testausetäisyys:",
    ["3 metriä (Kaukohaku)", "40 cm (Lähinäkö)"]
)

# --- TUOTEDATA (Koodit ja nimet) ---
# Tässä on logiikka suosituksille
st.subheader(f"Suositus: {ika} lapselle ({etaisyys})")

c1, c2 = st.columns([2, 1])

with c1:
    if ika == "0-6 kk":
        st.success("### Lea Grating Paddles (#251300)")
        st.write("""
        **Käyttö:** Vauvojen ja kehitysvammaisten näön tarkkuuden mittaamiseen hila-testillä. 
        Käytetään menetelmää, jossa seurataan lapsen katselusuunnan kohdistumista raitakuvioon.
        """)
        st.info("💡 *Vinkki: Lisää mukaan Hiding Heidi (#253500) matalan kontrastin tutkimiseen.*")
        linkki = "https://leatest.fi/products/lea-grating-paddles"

    elif ika == "6-12 kk":
        st.success("### Lea Grating Paddles tai Hiding Heidi (#253500)")
        st.write("""
        **Käyttö:** Tässä iässä kommunikaatio on elepohjaista. Matalan kontrastin testi (Hiding Heidi) 
        on erinomainen väline varhaisen näön käytön arviointiin.
        """)
        linkki = "https://leatest.fi/products/hiding-heidi-low-contrast-test"

    elif ika == "1-2 v":
        st.success("### Lea Symbols -palapeli (#251600) tai kortit (#251300)")
        st.write("""
        **Käyttö:** Lapsi opettelee vastaavuutta. Palapeli on konkreettinen tapa testata, 
        tunnistaako lapsi symbolit, vaikka hän ei osaisi vielä nimetä niitä.
        """)
        linkki = "https://leatest.fi/products/lea-symbols-puzzle"

    elif ika == "3-4 v":
        if tapa == "Yksittäiset symbolit (Jos rivi on liian vaikea)":
            st.warning("### Kehystetyt Lea-symbolit / Framed Symbols (#251700)")
            st.write("""
            **Syy valintaan:** Jos lapsella on vaikeuksia rivitestissä (Crowding-ilmiö), kehystetyt 
            symbolit tarjoavat rivitestin kaltaisen haasteen, mutta helpottavat kohdistamista.
            """)
            linkki = "https://leatest.fi/products/lea-single-symbol-book"
        else:
            st.success("### Lea Symbols -testikirja (#250600) tai taulu (#252500)")
            st.write("**Käyttö:** Standardi seulontatesti 3 metrin etäisyydelle. Sisältää rivitestin.")
            linkki = "https://leatest.fi/products/lea-symbols-chart-3m"

    elif ika == "5-7 v":
        if etaisyys == "40 cm (Lähinäkö)":
            st.success("### Lea Symbols -lähitesti (#250800)")
            st.write("**Käyttö:** Tarkka rivitesti lähityöskentelyn ja lukunäön arviointiin.")
            linkki = "https://leatest.fi/products/lea-symbols-near-vision-card"
        else:
            st.success("### Lea Symbols 15-rivinen taulu (#250000)")
            st.write("**Käyttö:** Virallinen kaukonäön testi seulontaan ja diagnostiikkaan.")
            linkki = "https://leatest.fi/products/lea-symbols-15-line-folding-chart"

with c2:
    st.write("### Tilaustiedot")
    st.metric("Suositeltu tuotekoodi", "LEA#" + linkki.split("-")[-1].upper() if "#" not in st.session_state else "Katso koodi")
    st.link_button("Siirry tuotteeseen 🛒", linkki)

st.divider()

# --- LISÄTIETOA NÄÖN KEHITYKSESTÄ ---
with st.expander("Lue lisää lapsen näön kehityksestä (0-7 v.)"):
    st.write("""
    * **0-3 kk:** Mustavalkoiset, suuret kuviot. Katseluetäisyys n. 25 cm.
    * **6 kk:** Värien ja syvyyden hahmotus kehittyy.
    * **1-2 v:** Hahmon tunnistus (ympyrä, neliö, talo, omena).
    * **3-4 v:** Kyky erottaa optotyyppejä rivistä alkaa vakiintua.
    * **5-7 v:** Näöntarkkuus saavuttaa aikuisten tason (1.0 tai enemmän).
    """)

st.caption("HUOM: Tämä valitsin on ammattilaisten apuväline. Tee lopullinen valinta aina kliinisen tarpeen mukaan.")
