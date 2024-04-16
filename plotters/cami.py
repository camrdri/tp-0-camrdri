import seaborn.objects as so
from gapminder import gapminder


def plot():
    figura = (
        so.Plot(
            gapminder[gapminder.continent == "America"],
            x="year",
            y="lifeExp",
            color="country",
        )
        .add(so.Line())
        .label(
            title="Expectativa de vida en America",
            x="Año",
            y="Expectativa de vida",
            color="País",
        )
    )
    return dict(
        descripcion="Expectativa de vida en países de America a lo largo del tiempo",
        autor="Cami",
        figura=figura,
    )
