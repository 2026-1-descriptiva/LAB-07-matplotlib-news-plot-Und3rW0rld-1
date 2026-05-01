"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import os

    import matplotlib

    matplotlib.use("Agg")

    import matplotlib.pyplot as plt
    import pandas as pd

    news = pd.read_csv("files/input/news.csv", index_col=0)
    news.index = news.index.astype(int)

    years = news.index.to_list()

    colors = {
        "Television": "#666666",
        "Newspaper": "#7A7A7A",
        "Radio": "#CFCFCF",
        "Internet": "#1F77B4",
    }

    fig, ax = plt.subplots(figsize=(6.4, 4.8))

    # Lines
    for column in ["Television", "Newspaper", "Radio", "Internet"]:
        linewidth = 3 if column == "Internet" else 2
        ax.plot(
            years,
            news[column],
            color=colors[column],
            linewidth=linewidth,
            solid_capstyle="round",
            zorder=2,
        )

        ax.scatter(
            [years[0], years[-1]],
            [news[column].iloc[0], news[column].iloc[-1]],
            color=colors[column],
            s=30,
            zorder=3,
        )

    # Title + subtitle
    ax.set_title("How people get their news", fontsize=18, pad=20)
    ax.text(
        0.5,
        1.02,
        "An increasing proportion cite the internet as their primary news source",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=9,
        color="#333333",
    )

    # Axis styling
    ax.set_xlim(years[0] - 0.5, years[-1] + 0.5)
    ax.set_ylim(0, 90)
    ax.set_xticks(years)
    ax.tick_params(axis="y", which="both", left=False, labelleft=False)
    ax.tick_params(axis="x", which="both", top=False)
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)

    # Left labels
    left_x = years[0] - 0.25
    ax.text(
        left_x,
        news["Television"].iloc[0],
        f"Television {news['Television'].iloc[0]}%",
        ha="right",
        va="center",
        fontsize=11,
        color=colors["Television"],
    )
    ax.text(
        left_x,
        news["Newspaper"].iloc[0],
        f"Newspaper {news['Newspaper'].iloc[0]}%",
        ha="right",
        va="center",
        fontsize=11,
        color=colors["Newspaper"],
    )
    ax.text(
        left_x,
        news["Radio"].iloc[0],
        f"Radio {news['Radio'].iloc[0]}%",
        ha="right",
        va="center",
        fontsize=11,
        color=colors["Radio"],
    )
    ax.text(
        left_x,
        news["Internet"].iloc[0],
        f"Internet {news['Internet'].iloc[0]}%",
        ha="right",
        va="center",
        fontsize=11,
        color=colors["Internet"],
    )

    # Right labels
    right_x = years[-1] + 0.25
    for column in ["Television", "Newspaper", "Radio", "Internet"]:
        ax.text(
            right_x,
            news[column].iloc[-1],
            f"{news[column].iloc[-1]}%",
            ha="left",
            va="center",
            fontsize=11,
            color=colors[column],
        )

    os.makedirs("files/plots", exist_ok=True)
    fig.tight_layout()
    fig.savefig("files/plots/news.png")
    plt.close(fig)
