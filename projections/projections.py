### Dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from navbar import Navbar
from footer import Footer

from projections.map import top_visual
from projections.timeline import bottom_visual

nav = Navbar()
footer = Footer()

body = dbc.Container(
    [
       dbc.Row(
        [
            dbc.Col(
            [
                html.H2("DELPHI Epidemiological Case Predictions""),
                dcc.Markdown("""\
                        A critical tool for COVID-19 planning is charting out the progression \
                        of the pandemic across the United States and the world. \
                        We've developed a new epidemiological model called DELPHI, which \
                        forecasts infections, hospitalizations, and deaths. \
                        You can think of our model as a standard \
                        [SEIR model](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology#The_SEIR_model) \
                        with additional \
                        features specific to the COVID-19 pandemic, like under-detection and \
                        differentiated government intervention.
                       """),
                dcc.Markdown('''If you want to learn more, check out the \
                             [documentation](/projections_documentation) or \
                             [source code](https://github.com/COVIDAnalytics/epidemic-model).'''),
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                            html.H5("Note: what do we mean by \"active cases\"?"),
                            dcc.Markdown("We define a COVID-19 case as **active** \
                                         if it has not yet resulted in recovery \
                                         or death. You may notice a discrepancy \
                                         between the number of active cases here \
                                         and on the \
                                         [JHU map](https://coronavirus.jhu.edu/map.html). \
                                         The JHU map is very good at keeping track of new cases, \
                                         but does not always publish data on recovered cases, \
                                         which can lead to overestimating currently active \
                                         cases."),
                            dcc.Markdown("**Disclaimer on total counts:** Our predictions only account \
                                         for countries in which we have sufficient data and where \
                                         the pandemic is currently active. \
                                         In particular, it excludes some East Asian countries \
                                         where the pandemic has passed."),
                            ]
                        ),
                    ],
                    className='projections-general-card'
                ),
            ]
            ),
        ],
        )
    ] + \
        top_visual + \
        bottom_visual,
   className="page-body"
)

def ProjectState():
    layout = html.Div([nav, body, footer],className="site")
    return layout
