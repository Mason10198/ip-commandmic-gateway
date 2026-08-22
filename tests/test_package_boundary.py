from pathlib import Path

import ip_commandmic_gateway
from ip_commandmic_gateway import GatewayConfig
from ip_commandmic_gateway.app import main


def test_public_scaffold_identity_and_safe_defaults() -> None:
    assert ip_commandmic_gateway.__version__ == "0.1.0a1"
    config = GatewayConfig()
    config.validate()
    assert config.host == "127.0.0.1"
    assert config.enable_ptt is False
    assert config.allow_remote_clients is False


def test_remote_client_configuration_requires_non_loopback_bind() -> None:
    config = GatewayConfig(allow_remote_clients=True)
    try:
        config.validate()
    except ValueError as error:
        assert "non-loopback" in str(error)
    else:
        raise AssertionError("unsafe remote-client configuration was accepted")


def test_scaffold_cli_only_validates_without_starting_services(capsys) -> None:
    assert main(["--check-config"]) == 0
    assert "valid" in capsys.readouterr().out


def test_retired_web_namespace_is_absent() -> None:
    assert not (Path(__file__).parents[1] / "src" / "ip_commandmic_web").exists()
