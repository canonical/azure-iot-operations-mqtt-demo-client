from setuptools import setup

setup(
    name="mqtt-client",
    python_requires=">=3.10",
    install_requires=[
        "annotated-types==0.7.0",
        "paho-mqtt==2.1.0",
        "pydantic==2.8.2",
        "pydantic_core==2.20.1",
        "typing_extensions==4.12.2",
    ],
    packages=["mqtt_client"],
    entry_points={
        "console_scripts": ["mqtt-client-cli=mqtt_client.client:main"],
    },
)
