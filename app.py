# ------------------------------------------------------------
# STREAMLIT DASHBOARD - UNIVERSITY STUDENT DATA
# Universidad de la Costa - Data Mining
# Autor: Juan Pablo Cristancho Gonzalez
# ------------------------------------------------------------

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="University Dashboard", layout="wide")

# Cargar datos
df = pd.read_csv("university_student_data.csv")

# Limpieza de nombres (quitar espacios, paréntesis y símbolos %)
df.columns = (
    df.columns.str.strip()
              .str.replace(" ", "_")
              .str.replace("(", "")
              .str.replace(")", "")
              .str.replace("%", "")
)

# Título principal
st.title("🎓 University Student Dashboard")
st.markdown("Visualización simple de retención, satisfacción y matrícula universitaria")

# Filtros interactivos
col1, col2 = st.columns(2)
year = col1.selectbox("Selecciona el Año:", sorted(df["Year"].unique()))
term = col2.selectbox("Selecciona el Periodo Académico:", df["Term"].unique())

# Filtrar datos
filtered_df = df[(df["Year"] == year) & (df["Term"] == term)]

# Mostrar datos filtrados
st.subheader(f"📊 Datos del {term} - Año {year}")
st.dataframe(filtered_df)

# Métricas principales
col1, col2, col3 = st.columns(3)
col1.metric("Retention Rate", f"{filtered_df['Retention_Rate_'].mean():.1f}%")
col2.metric("Satisfaction", f"{filtered_df['Student_Satisfaction_'].mean():.1f}%")
col3.metric("Enrolled Students", int(filtered_df["Enrolled"].sum()))

st.markdown("---")

# Gráfico 1: Retención por año
st.subheader("📈 Tendencia de Retención por Año")
fig1, ax1 = plt.subplots()
sns.lineplot(data=df, x="Year", y="Retention_Rate_", marker="o", ax=ax1)
ax1.set_title("Retention Rate (%) Over Time")
st.pyplot(fig1)

# Gráfico 2: Satisfacción por año
st.subheader("🌟 Promedio de Satisfacción por Año")
fig2, ax2 = plt.subplots()
sns.barplot(data=df, x="Year", y="Student_Satisfaction_", palette="viridis", ax=ax2)
ax2.set_title("Student Satisfaction by Year")
st.pyplot(fig2)

# Gráfico 3: Comparación Spring vs Fall
st.subheader("🍂 Comparación de Retención: Spring vs Fall")
fig3, ax3 = plt.subplots()
sns.boxplot(data=df, x="Term", y="Retention_Rate_", palette="pastel", ax=ax3)
ax3.set_title("Retention Rate by Term")
st.pyplot(fig3)

st.markdown("---")
st.caption("Dashboard desarrollado con ❤️ usando Streamlit y Python")
