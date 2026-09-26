import json

log_path = r'C:\Users\manoj\.gemini\antigravity-ide\brain\206ca220-6a19-43f1-8d82-85714be15932\.system_generated\logs\transcript_full.jsonl'
with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        if '"name":"write_to_file"' in line and 'styles.css' in line and 'CodeContent' in line:
            try:
                data = json.loads(line)
                args = data['tool_calls'][0]['args']
                if 'styles.css' in args.get('TargetFile', ''):
                    with open('styles.css', 'w', encoding='utf-8') as out:
                        out.write(args['CodeContent'])
            except Exception as e:
                pass
