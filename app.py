import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json

# Cargar los datos
@st.cache
def load_data(filename):
    with open(filename) as f:
        data = json.load(f)
    return data

data_ggs = load_data('ggs 1.json')  # Ajusta el nombre del archivo según sea necesario

# Visualización 1: Resumen de torneos
def show_tournament_summary(data):
    st.header("Resumen del Torneo")
    st.write(f"Nombre: {data['event']['name']}")
    st.write(f"Fecha: {data['event']['date']}")
    st.write(f"Participantes: {data['event']['numberEntrants']}")
    st.write(f"[Enlace al Torneo]({data['event']['originURL']})")

# Visualización 2: Resultados de los partidos
def show_matches(data):
    st.header("Resultados de los Partidos")
    matches = pd.DataFrame(data['sets'])
    st.write(matches[['entrant1ID', 'entrant2ID', 'entrant1Result', 'entrant2Result', 'entrant1Score', 'entrant2Score']])

# Visualización 3: Ranking de jugadores
def show_player_rankings(data):
    st.header("Ranking de Jugadores")
    entrants = pd.DataFrame(data['entrants'])
    rankings = entrants.sort_values(by='finalPlacement')
    st.write(rankings[['entrantTag', 'finalPlacement']])

# Visualización 4: Gráficos
def plot_player_performance(data):
    st.header("Desempeño de los Jugadores")
    entrants = pd.DataFrame(data['entrants'])
    fig, ax = plt.subplots()
    entrants['finalPlacement'].hist(bins=20, ax=ax)
    ax.set_title('Histograma de Posiciones Finales')
    ax.set_xlabel('Posición Final')
    ax.set_ylabel('Frecuencia')
    st.pyplot(fig)

# Layout del Dashboard
def main():
    st.title("Dashboard de Torneos")
    show_tournament_summary(data_ggs)
    show_matches(data_ggs)
    show_player_rankings(data_ggs)
    plot_player_performance(data_ggs)

if __name__ == "__main__":
    main()
