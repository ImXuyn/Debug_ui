from setuptools import setup

package_name = "debug_ui"

setup(
    name=package_name,
    version="0.0.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        ("share/" + package_name, ["launch/launch.py"]),
        ("share/" + package_name + "/static", [f"{package_name}/static/index.html"]),
        ("share/" + package_name + "/static", [f"{package_name}/static/style.css"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="njames",
    maintainer_email="nick.james@dorabot.com",
    description="TODO: Package description",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={"console_scripts": ["main=debug_ui.main:main"]},
)
