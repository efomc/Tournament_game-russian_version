from setuptools import setup, find_packages

import tournament_game

install_requires = [
    'pytest>=6.2.5',
    'setuptools>=56.0.0',
]

setup(
    name='Tournament_game',
    version=tournament_game.__version__,
    license='MIT License',
    packages=find_packages(),
    description='fight tournament game',
    long_description=(
        'Игра моделирует турнир между бойцами из произвольных наборов или созданных пользователем. '
        'Пользователь может делать ставки на победителя поединков и/или турнира, '
        'занимать место в таблице достижений и улучшать его.'),

    author='Egor Fomin, beresk_let',
    author_email='fomc@inbox.ru',
    url='https://github.com/efomc/',

    entry_points={
        'console_scripts':
            ['tournamentgame = tournament_game.core:main']
        },

    test_suite='tests',
)



