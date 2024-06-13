import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Carregando o excel
df = pd.read_excel("Dados.xlsx")

# Ordenando o DataFrame
df = df.sort_values(by=['id_data', 'id_valor'])


df = df.rename(columns={'id_valor': 'Valor', 'id_data': 'Data', 'count': 'Contagem', 'id_destino': 'Destino', 'id_origem': 'Origem'})


cores = {
    'background': '#FFFFFF',  # branco
    'text': '#000000',  # preto
    'plot_color': '#3CB371'  # verde médio
}

# Paleta de cores
paleta_cores_origem = {'Origem': {'Amarelo': '#FFFF00', 'Verde': '#008000', 'Vermelho': '#FF0000', 'Azul': '#0000FF', 'Roxo': '#800080'}}


paleta_cores_destino = {'Destino': {'Azul': '#0000FF', 'Preto': '#000000'}}


app = dash.Dash(__name__)

# Layout
app.layout = html.Div(style={'backgroundColor': cores['background'], 'color': cores['text']}, children=[
    html.H1(
        children='Análise Financeira',
        style={
            'textAlign': 'center',
            'color': cores['text']
        }
    ),

    html.Div([
        dcc.Graph(
            id='grafico-valor-tempo',
            figure=px.line(df, x='Data', y='Valor', title='Valor ao Longo do Tempo', color_discrete_sequence=[cores['plot_color']])
                    .update_layout(
                        xaxis_title='Data',
                        yaxis_title='Valor',
                        legend_title=None,
                        font=dict(family='Arial, sans-serif', size=12),
                        title_font=dict(size=20)
                    )
        )
    ], style={'width': '50%', 'display': 'inline-block', 'padding': '20px'}),

    html.Div([
        dcc.Graph(
            id='grafico-origem',
            figure=px.pie(df, names='Origem', title='Distribuição por Origem', color_discrete_map=paleta_cores_origem['Origem'])
                    .update_traces(textposition='inside', textinfo='percent+label')
                    .update_layout(
                        legend_title=None,
                        font=dict(family='Arial, sans-serif', size=12),
                        title_font=dict(size=20)
                    )
        )
    ], style={'width': '45%', 'display': 'inline-block', 'padding': '20px', 'margin-left': '10px'}),

    html.Div([
        dcc.Graph(
            id='grafico-destino',
            figure=px.histogram(df, x='Destino', title='Distribuição por Destino', color_discrete_map=paleta_cores_destino['Destino'])
                    .update_layout(
                        xaxis_title='Destino',
                        yaxis_title='Contagem',
                        barmode='group',
                        legend_title=None,
                        font=dict(family='Arial, sans-serif', size=12),
                        title_font=dict(size=20)
                    )
        )
    ], style={'width': '97%', 'padding': '20px', 'margin-top': '20px'})
])

# Rodando o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)

