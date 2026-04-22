import streamlit as st

st.set_page_config(page_title="Lea-testin valitsin", page_icon="📋")

st.title("📋 Löydä oikea Lea-testi")
st.write("Vastaa muutamaan kysymykseen, niin suosittelemme tarpeisiisi parhaiten sopivaa välinettä.")

# --- KYSYMYKSET ---
st.sidebar.header("Valintakriteerit")

ika = st.radio(
    "1. Ketä testataan?",
    ["Vauva (0-12 kk)", "Leikki-ikäinen (1-6 v.)", "Koululainen tai aikuinen"]
)

etaisyys = st.radio(
    "2. Millä etäisyydellä testi halutaan tehdä?",
    ["Lähinäkö (40 cm)", "Kaukonäkö (3 metriä)", "En tiedä vielä"]
)

tarkoitus = st.radio(
    "3. Mikä on testauksen päätavoite?",
    ["Perusseulonta (Näöntarkkuus)", "Kontrastinherkkyyden tutkiminen", "Diagnostiikka / Syvällinen tutkimus"]
)

st.divider()

# --- LOGIIKKA JA SUOSITUKSET ---
st.subheader("Suosituksemme:")

if ika == "Vauva (0-12 kk)":
    st.success("Suosittelemme: **Lea Grating -testi (Hila-testi)**")
    st.write("Vauvojen näön tutkimiseen soveltuu parhaiten preferentiaalisen katselun testi.")
    st.link_button("Katso tuote kaupassa", "https://leatest.fi")

elif ika == "Leikki-ikäinen (1-6 v.)" and etaisyys == "Kaukonäkö (3 metriä)":
    st.success("Suosittelemme: **Lea Symbols -taulu (3 metriä)**")
    st.write("Tämä on standarditesti leikki-ikäisten seulontaan 3 metrin etäisyydeltä.")
    st.link_button("Osta tästä", "https://leatest.fi")

elif tarkoitus == "Kontrastinherkkyyden tutkiminen":
    st.success("Suosittelemme: **Lea Low Contrast -testit**")
    st.write("Matala kontrasti antaa tärkeää tietoa lapsen kyvystä havaita hahmoja sumussa tai hämärässä.")
    st.link_button("Tutustu kontrastitesteihin", "https://leatest.fi")

else:
    st.info("Tarpeesi ovat yksilölliset. Suosittelemme monikäyttöistä **Lea Symbols 15-rivistä taulua**.")
    st.link_button("Lue lisää", "https://leatest.fi")

st.divider()
st.caption("Tarvitsetko apua valinnassa? Ota yhteyttä info@leatest.fi")
