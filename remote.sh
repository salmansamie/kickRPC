

fetch_config() {
    local running_config=$(tmsh show running-config recursive)
    echo "$running_config"
}

fetch_config
