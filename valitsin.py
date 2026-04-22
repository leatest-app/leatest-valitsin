import streamlit as st

st.set_page_config(page_title="Lea-testin valitsin", page_icon="📋", layout="wide")

# --- KIELIVALINTA ---
kieli = st.sidebar.radio("Valitse kieli / Välj språk / Select Language", ["Suomi", "Svenska", "English"])

# --- TEKSTIDATA (Lokalisoitu) ---
t = {
    "Suomi": {
        "title": "📋 Lea-testin ammattilaisvalitsin",
        "intro": "Löydä oikea testiväline lapsen iän ja kehitystason mukaan.",
        "sidebar_hdr": "Testaustilanne",
        "age_label": "Lapsen ikä:",
        "dist_label": "Testausetäisyys:",
        "method_label": "Testaustapa:",
        "method_opts": ["Rivitesti (Standardi)", "Yksittäiset symbolit (Crowding / Ahtausilmiö)"],
        "inf_age": "Alle 2-vuotiaille suositellaan lähitestausta.",
        "near_only": "Lähitesti / Kommunikaatioetäisyys",
        "dist_3m": "Kaukonäkö (3 m)",
        "near_40cm": "Lähinäkö (40 cm)",
        "rec_hdr": "Suositus:",
        "buy_btn": "Katso tuote kaupassa",
        "code_label": "Tuotekoodi:",
        "exp_hdr": "ℹ️ Ohjeita testin valintaan",
        "exp_txt": "Rivitesti on vaativampi. Jos lapsi hukkaa rivin, käytä kehystettyjä yksittäissymboleita. Vauvoille käytetään aina hila-testejä (Grating)."
    },
    "Svenska": {
        "title": "📋 Lea-test väljare",
        "intro": "Hitta rätt testverktyg baserat på barnets ålder och utvecklingsnivå.",
        "sidebar_hdr": "Testsituation",
        "age_label": "Barnets ålder:",
        "dist_label": "Testavstånd:",
        "method_label": "Testmetod:",
        "method_opts": ["Radtest (Standard)", "Enskilda symboler (Crowding)"],
        "inf_age": "För barn under 2 år rekommenderas närtest.",
        "near_only": "Närtest / Kommunikationsavstånd",
        "dist_3m": "Avståndssyn (3 m)",
        "near_40cm": "Närsyn (40 cm)",
        "rec_hdr": "Rekommendation:",
        "buy_btn": "Visa produkten i butiken",
        "code_label": "Produktkod:",
        "exp_hdr": "ℹ️ Instruktioner för val av test",
        "exp_txt": "Radtest är mer krävande. Om barnet tappar raden, använd inramade enskilda symboler."
    },
    "English": {
        "title": "📋 Lea Test Selector",
        "intro": "Find the right testing tool based on the child's age and developmental level.",
        "sidebar_hdr": "Testing Situation",
        "age_label": "Child's age:",
        "dist_label": "Testing distance:",
        "method_label": "Testing method:",
        "method_opts": ["Line test (Standard)", "Single symbols (Crowding)"],
        "inf_age": "Near testing is recommended for children under 2 years.",
        "near_only": "Near test / Communication distance",
        "dist_3m": "Distance vision (3 m)",
        "near_40cm": "Near vision (40 cm)",
        "rec_hdr": "Recommendation:",
        "buy_btn": "View product in store",
        "code_label": "Product code:",
        "exp_hdr": "ℹ️ Tips for selection",
        "exp_txt": "Line tests are more demanding. If the child loses their place, use framed single symbols."
    }
}

txt = t[kieli]

st.title(txt["title"])
st.write(txt["intro"])

# --- SIVUPALKKI ---
st.sidebar.header(txt["sidebar_hdr"])

ika_opts = ["0-6 kk", "6-12 kk", "1-2 v", "2.5-3 v", "3-4 v", "4-7 v"]
ika = st.sidebar.select_slider(txt["age_label"], options=ika_opts)

if ika in ["0-6 kk", "6-12 kk", "1-2 v"]:
    etaisyys = txt["near_only"]
    st.sidebar.info(txt["inf_age"])
else:
    etaisyys = st.sidebar.radio(txt["dist_label"], [txt["dist_3m"], txt["near_40cm"]])

tapa = st.sidebar.radio(txt["method_label"], txt["method_opts"])

# --- APUFUNKTIO ---
def nayta_tuote(nimi, koodi, kuvaus, linkki_handle, kuva_url):
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image(kuva_url, use_container_width=True)
    with c2:
        st.success(f"### {nimi}")
        st.write(f"**{txt['code_label']}** #{koodi}")
        st.write(kuvaus)
        url = f"https://leatest.fi/products/{linkki_handle}"
        st.link_button(txt["buy_btn"], url)

st.divider()
st.subheader(f"{txt['rec_hdr']} {ika} ({etaisyys})")

# --- SUOSITUKSET ---
# Huom: Päivitä kuva_url ja linkki_handle kauppasi mukaan
if ika == "0-6 kk":
    nayta_tuote(
        "LEA GRATINGS® – näöntarkkuustesti – mela-setti", "253300",
        "Vauvojen ja kehitysvammaisten näöntarkkuuden mittaamiseen hila-testillä.",
        "lea-gratings-naontarkkuustesti-mela-setti", # KORJATTU LINKKI
        "https://leatest.fi/cdn/shop/files/253300_1_800x.jpg" # Esimerkkikuva
    )

elif ika == "6-12 kk":
    nayta_tuote(
        "Hiding Heidi – matalan kontrastin testi", "253500",
        "Arvioi viestintäetäisyyden ja kasvojen tunnistamisen matalalla kontrastilla.",
        "hiding-heidi-matalan-kontrastin-testi",
        "https://leatest.fi/cdn/shop/files/253500_1_800x.jpg"
    )

elif ika == "1-2 v":
    nayta_tuote(
        "LEA SYMBOLS® -palapeli", "251600",
        "Opeta symbolit leikin kautta ennen varsinaista testausta.",
        "lea-symbols-palapeli",
        "https://leatest.fi/cdn/shop/files/251600_1_800x.jpg"
    )

elif ika == "2.5-3 v":
    if etaisyys == txt["near_40cm"]:
        nayta_tuote("LEA SYMBOLS® -lähitesti", "250800", "Lähinäön tutkimiseen 40 cm etäisyydeltä.", "lea-symbols-lahitesti", "https://leatest.fi/cdn/shop/files/250800_1_800x.jpg")
    else:
        nayta_tuote("LEA SYMBOLS® -taulu (3 m)", "250250", "10-rivinen taulu kaukoseulontaan.", "lea-symbols-taulu-3m-10-rivia", "https://leatest.fi/cdn/shop/files/250250_1_800x.jpg")

elif ika in ["3-4 v", "4-7 v"]:
    if tapa == txt["method_opts"][1]: # Yksittäiset symbolit
        nayta_tuote("LEA SYMBOLS® -yksittäissymbolit (kirja)", "250600", "Kehystetyt symbolit lapsille, joilla on ahtausilmiö (crowding).", "lea-symbols-yksittaissymbolit-testikirja", "https://leatest.fi/cdn/shop/files/250600_1_800x.jpg")
    else:
        koodi = "250250" if ika == "3-4 v" else "250150"
        handle = "lea-symbols-taulu-3m-10-rivia" if ika == "3-4 v" else "lea-symbols-taulu-3m-15-rivia"
        nayta_tuote(f"LEA SYMBOLS® -taulu ({koodi})", koodi, "Standardi seulontataulu kaukonäön tutkimiseen.", handle, f"https://leatest.fi/cdn/shop/files/{koodi}_1_800x.jpg")

st.divider()
with st.expander(txt["exp_hdr"]):
    st.write(txt["exp_txt"])
