module.exports = {
  apps : [{
    name: 'NGram',
    script: 'main.py',
    interpreter: 'python3',
    log_file: 'NGram.log',
    min_uptime: 5000,
    kill_timeout: 15000,
    max_restarts: 3,

    exec_mode: "fork",

    args: '-u',
    instances: 1,
    autorestart: true,
    watch: false,
    max_memory_restart: '7000M',
  }
  ]
};