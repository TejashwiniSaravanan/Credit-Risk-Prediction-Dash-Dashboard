import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html

# Load your data
file_path = r"C:\Users\Tejashwini Saravanan\Credit Risk Data.xlsx"
base_df = pd.read_excel(file_path, sheet_name="Base Data")

# CHART 1: Gender Split (fix applied)
gender_count = base_df["Gender"].value_counts().reset_index()
gender_count.columns = ["Gender", "Count"]
fig_gender = px.bar(
    gender_count,
    x="Gender", y="Count",
    title="Gender Split of Customers",
    color="Gender",
    color_discrete_sequence=["#FF69B4", "#6495ED"]
)

# CHART 2: Age Distribution
fig_age = px.histogram(base_df, x="Age", nbins=20, title="Age Distribution")

# CHART 3: Female Age by Marital Status
female_df = base_df[base_df["Gender"] == "F"]
fig_female_age = px.histogram(
    female_df, x="Age", color="Marital Status",
    nbins=20, barmode="overlay",
    title="Female Age by Marital Status"
)

# CHART 4: Male Homeowners Age
male_own_df = base_df[(base_df["Gender"] == "M") & (base_df["Housing"] == "Own")]
fig_male_home = px.histogram(
    male_own_df, x="Age", nbins=20,
    title="Male Homeowners - Age Distribution",
    color_discrete_sequence=["#4169E1"]
)

# DASH APP
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Credit Risk Analysis Dashboard", style={'textAlign': 'center'}),

    html.Div([
        dcc.Graph(figure=fig_gender),
        dcc.Graph(figure=fig_age),
        dcc.Graph(figure=fig_female_age),
        dcc.Graph(figure=fig_male_home),
    ])
])

if __name__ == '__main__':
    app.run(debug=True)




