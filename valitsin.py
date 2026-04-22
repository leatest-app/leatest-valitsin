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
        "buy_btn": "Tilaa tuote kaupasta 🛒",
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
        "buy_btn": "Beställ produkten i butiken 🛒",
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
        "buy_btn": "Order product from store 🛒",
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

# Määritetään etäisyysvalinnat
if ika in ["0-6 kk", "6-12 kk", "1-2 v"]:
    etaisyys = txt["near_only"]
    st.sidebar.info(txt["inf_age"])
else:
    etaisyys = st.sidebar.radio(txt["dist_label"], [txt["dist_3m"], txt["near_40cm"]])

# Määritetään testaustapa (Rivitesti vs Yksittäiset)
tapa = st.sidebar.radio(txt["method_label"], txt["method_opts"])

# --- APUFUNKTIO ---
def nayta_tuote(nimi, koodi, kuvaus, tuote_url, kuva_url):
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image(kuva_url, use_container_width=True)
    with c2:
        st.success(f"### {nimi}")
        st.write(f"**{txt['code_label']}** #{koodi}")
        st.write(kuvaus)
        st.link_button(txt["buy_btn"], tuote_url)

st.divider()
st.subheader(f"{txt['rec_hdr']} {ika} ({etaisyys} / {tapa})")

# --- TUOTETIEDOT (Dynaamisesti haetut URLit ja kuvat) ---

# 1. Tuote 253300 (Hila)
URL_253300 = "https://leatest.fi/products/goodlite-253300-paddles-lea-gratings-a-preferential-looking-test-set"
IMG_253300 = "https://leatest.fi/cdn/shop/files/good-lite-vision-testing-aids-paddles-lea-gratings-a-preferential-looking-test-set-paddles-lea-gratings-a-preferential-looking-test-253300-1197849552.jpg?v=1771344288&width=823"

# 2. Tuote 253500 (Heidi)
URL_253500 = "https://leatest.fi/products/goodlite-253500-cards-hiding-heidi-low-contrast-face-test-double-sided"
IMG_253500 = "https://leatest.fi/cdn/shop/files/good-lite-253510-single-sided-hiding-heidi-low-contrast-face-test-253510-31346832310377.jpg?v=1771344291&width=823"

# 3. Tuote 251600 (Palapeli)
URL_251600 = "https://leatest.fi/products/goodlite-251600-response-panel-lea-symbols-3-d-puzzle-set"
IMG_251600 = "https://leatest.fi/cdn/shop/files/good-lite-lea-3-d-puzzle-251600-31895201841257.jpg?v=1771344277&width=823"

# 4. Tuote 250800 (Lähikortti)
URL_250800 = "https://leatest.fi/products/goodlite-250800-cardnear-lea-symbols-near-vision-card-with-cord-16-40cm"
IMG_250800 = "https://leatest.fi/cdn/shop/files/good-lite-co-lea-symbols-near-vision-card-250800-32461354664041.jpg?v=1772825481&width=823"

# 5. Tuote 250250 (10-rivinen)
URL_250250 = "https://leatest.fi/products/goodlite-250250-folding-chart-lea-symbols-10-line-black-back-set-10ft-3m"
IMG_250250 = "https://leatest.fi/cdn/shop/files/good-lite-lea-symbols-sup-sup-10-line-distance-charts-250250-31306945167465.jpg?v=1771344268&width=823"

# 6. Tuote 250600 (Yksittäissymbolit)
URL_250600 = "https://leatest.fi/products/goodlite-250600-flip-book-lea-symbols-single-symbol-book-set-10ft-3m"
IMG_250600 = "https://leatest.fi/cdn/shop/files/good-lite-lea-symbols-sup-sup-single-symbol-book-250600-31306945200233.jpg?v=1771344270&width=823"

# 7. Tuote 250150 (15-rivinen)
URL_250150 = "https://leatest.fi/products/goodlite-250150-folding-chart-lea-symbols-15-line-black-back-set-10ft-3m"
IMG_250150 = "https://leatest.fi/cdn/shop/files/good-lite-lea-symbols-sup-sup-15-line-distance-chart-250150-31306944938089.jpg?v=1771344265&width=823"

# --- SUOSITUSLOGIIKKA (Korjattu ja suoraviivaistettu) ---

if ika == "0-6 kk":
    nayta_tuote("LEA GRATINGS® – hila-testi", "253300", "Vauvojen ja kehitysvammaisten näöntarkkuuden mittaamiseen.", URL_253300, IMG_253300)

elif ika == "6-12 kk":
    nayta_tuote("Hiding Heidi – matalan kontrastin testi", "253500", "Viestintäetäisyyden ja kasvojen tunnistamisen arviointiin.", URL_253500, IMG_253500)

elif ika == "1-2 v":
    nayta_tuote("LEA SYMBOLS® -palapeli", "251600", "Opeta symbolit leikin kautta ennen varsinaista testausta.", URL_251600, IMG_251600)

elif ika == "2.5-3 v":
    if etaisyys == txt["near_40cm"]:
        nayta_tuote("LEA SYMBOLS® -lähitesti", "250800", "Lähinäön tutkimiseen 40 cm etäisyydeltä.", URL_250800, IMG_250800)
    elif tapa == txt["method_opts"][1]: # Yksittäiset symbolit
        nayta_tuote("LEA SYMBOLS® -yksittäissymbolit (kirja)", "250600", "Suositellaan Crowding-ilmiön tutkimiseen.", URL_250600, IMG_250600)
    else: # Kaukonäkö 3m + Rivitesti
        nayta_tuote("LEA SYMBOLS® -taulu (10 riviä)", "250250", "10-rivinen taulu kaukoseulontaan 3 metrin etäisyydelle.", URL_250250, IMG_250250)

elif ika == "3-4 v":
    if etaisyys == txt["near_40cm"]:
        nayta_tuote("LEA SYMBOLS® -lähitesti", "250800", "Lähinäön tutkimiseen 40 cm etäisyydeltä.", URL_250800, IMG_250800)
    elif tapa == txt["method_opts"][1]: # Yksittäiset symbolit
        nayta_tuote("LEA SYMBOLS® -yksittäissymbolit (kirja)", "250600", "Suositellaan Crowding-ilmiön tutkimiseen.", URL_250600, IMG_250600)
    else: # Kaukonäkö 3m + Rivitesti
        nayta_tuote("LEA SYMBOLS® -taulu (10 riviä)", "250250", "Standardi 10-rivinen taulu kaukoseulontaan.", URL_250250, IMG_250250)

elif ika == "4-7 v":
    if etaisyys == txt["near_40cm"]:
        nayta_tuote("LEA SYMBOLS® -lähitesti", "250800", "Lähinäön tutkimiseen 40 cm etäisyydeltä.", URL_250800, IMG_250800)
    elif tapa == txt["method_opts"][1]: # Yksittäiset symbolit
        nayta_tuote("LEA SYMBOLS® -yksittäissymbolit (kirja)", "250600", "Suositellaan Crowding-ilmiön tutkimiseen.", URL_250600, IMG_250600)
    else: # Kaukonäkö 3m + Rivitesti
        nayta_tuote("LEA SYMBOLS® -taulu (15 riviä)", "250150", "Tarkempi 15-rivinen taulu vanhemmille lapsille.", URL_250150, IMG_250150)

st.divider()
with st.expander(txt["exp_hdr"]):
    st.write(txt["exp_txt"])

st.caption("Päivitetty logiikka 2026. Leatest.fi")
