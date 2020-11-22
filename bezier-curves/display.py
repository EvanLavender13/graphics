import plotly.express as px
import plotly.graph_objects as go

colors = px.colors.qualitative.Plotly


def create_figure():
    fig = go.Figure()

    fig.update_layout(
        showlegend=False,
        margin=dict(
            l=25,
            r=25,
            t=50,
            b=50
        )
    )

    fig.update_xaxes(
        range=[-0.1, 1.1],
        constrain="domain",
        showticklabels=False,
        showgrid=False,
        zeroline=False,
    )

    fig.update_yaxes(
        range=[-0.1, 1.1],
        constrain="domain",
        showticklabels=False,
        showgrid=False,
        zeroline=False,
        scaleanchor="x",
        scaleratio=1
    )

    return fig


def add_control_points(figure, points):
    figure.add_trace(go.Scatter(
        x=points[:, 0],
        y=points[:, 1],
        mode="markers",
        marker=dict(size=[25] * points.shape[0],
                    color="red")
    ))


def add_curve(figure, points):
    figure.add_trace(go.Scatter(
        x=points[:, 0],
        y=points[:, 1],
        mode="lines+markers",
        marker=dict(size=[15] * (points.shape[0] + 1),
                    color="blue")
    ))


def add_line(figure, p0, p1, i):
    figure.add_trace(go.Scatter(
        x=[p0[0], p1[0]],
        y=[p0[1], p1[1]],
        mode="lines+markers",
        marker=dict(size=[15, 15],
                    color=colors[i % 10])
    ))
