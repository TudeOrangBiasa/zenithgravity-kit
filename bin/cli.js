#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Read the package.json to get the version
const packageJsonPath = path.join(__dirname, '../package.json');
const packageJson = JSON.parse(fs.readFileSync(packageJsonPath, 'utf8'));

const version = packageJson.version;

const args = process.argv.slice(2);
const command = args[0];

function printHelp() {
  console.log(`
🚀 Zenithgravity-kit CLI v${version}

Usage:
  npx zenithgravity <command>

Commands:
  init      Initialize the .agent directory in your current project.
            (Copies the kit's rules, skills, memory, and workflows).
  sync      Run the memory sync script in the current project to update
            the AI's design memory based on local package.json dependencies.
  help      Show this help message.
`);
}

if (!command || command === 'help') {
  printHelp();
  process.exit(0);
}

if (command === 'init') {
  const sourceAgentDir = path.join(__dirname, '..', '.agent');
  const targetAgentDir = path.join(process.cwd(), '.agent');

  if (fs.existsSync(targetAgentDir)) {
    console.error('❌ Error: .agent directory already exists in the current project.');
    console.error('If you want to re-initialize, please remove the existing .agent directory first.');
    process.exit(1);
  }

  try {
    // Node 16.7.0+ supports fs.cpSync
    if (fs.cpSync) {
        fs.cpSync(sourceAgentDir, targetAgentDir, { recursive: true });
    } else {
        // Fallback for older nodes if necessary, but CP sync is standard now
        console.error('❌ Error: Node.js v16.7.0 or higher is required for fs.cpSync.');
        process.exit(1);
    }
    
    console.log('✅ Zenithgravity-kit v${version} successfully initialized!');
    console.log('📁 The .agent directory has been copied to your project.');
    console.log('You can now use Zenithgravity Agentic workflows in this workspace.');
  } catch (err) {
    console.error('❌ Error copying .agent directory:', err);
    process.exit(1);
  }
} else if (command === 'sync') {
  const scriptsDir = path.join(process.cwd(), '.agent', 'scripts');
  const syncScript = path.join(scriptsDir, 'sync_memory.py');
  
  if (fs.existsSync(syncScript)) {
    console.log('🔄 Running Zenithgravity Memory Sync...');
    try {
        // Try to execute the python script
        execSync(`python3 ${syncScript}`, { stdio: 'inherit' });
    } catch (err) {
        // Fallback to 'python' if 'python3' is not mapped
        try {
            execSync(`python ${syncScript}`, { stdio: 'inherit' });
        } catch (fallbackErr) {
            console.error('❌ Error executing sync_memory.py. Make sure Python is installed.');
            process.exit(1);
        }
    }
  } else {
    console.error('❌ Error: .agent/scripts/sync_memory.py not found.');
    console.error('Did you run "npx zenithgravity init" in this project first?');
    process.exit(1);
  }
} else {
  console.error(`❌ Unknown command: ${command}`);
  printHelp();
  process.exit(1);
}
