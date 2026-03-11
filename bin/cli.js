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
🚀 \x1b[1mZenithgravity-kit CLI v${version}\x1b[0m

\x1b[36mUsage:\x1b[0m
  npx zenithgravity <command> [options]
  zenithgravity <command> [options] (if installed globally)

\x1b[36mCommands:\x1b[0m
  init      Initialize the .agent directory in your current project.
            \x1b[90m(Copies or merges the kit's rules, skills, memory, and workflows without deleting external skills).\x1b[0m
  sync      Run the memory sync script to update the AI's design memory
            \x1b[90m(Reads local package.json dependencies).\x1b[0m
  readme    Display the contents of the Zenithgravity-kit README.
  help      Show this help message.

\x1b[36mOptions:\x1b[0m
  -v, --version  Show the version number.
  -h, --help     Show this help message.
`);
}

// Support for version and help flags
if (args.includes('--version') || args.includes('-v')) {
  console.log(`v${version}`);
  process.exit(0);
}

if (args.includes('--help') || args.includes('-h') || !command || command === 'help') {
  printHelp();
  process.exit(0);
}

if (command === 'init') {
  const sourceAgentDir = path.join(__dirname, '..', '.agent');
  const targetAgentDir = path.join(process.cwd(), '.agent');

  if (fs.existsSync(targetAgentDir)) {
    console.log('\x1b[33m%s\x1b[0m', 'ℹ️  .agent directory already exists. Unifying and merging Zenithgravity-kit files...');
    console.log('\x1b[90m%s\x1b[0m', '   (External skills and custom files will NOT be deleted)');
  } else {
    console.log('\x1b[36m%s\x1b[0m', 'Creating .agent directory structure...');
  }

  try {
    // Node 16.7.0+ supports fs.cpSync
    if (fs.cpSync) {
        fs.cpSync(sourceAgentDir, targetAgentDir, { recursive: true });
    } else {
        // Fallback for older nodes if necessary, but CP sync is standard now
        console.error('Error: Node.js v16.7.0 or higher is required for fs.cpSync.');
        process.exit(1);
    }
    
    console.log(`\n✅ \x1b[32m\x1b[1mZenithgravity-kit v${version} successfully initialized!\x1b[0m`);
    console.log('The .agent directory is ready in your workspace.');
    console.log('You can now use Zenithgravity Agentic workflows and Impeccable skills.');
  } catch (err) {
    console.error('\n❌ \x1b[31mError copying .agent directory:\x1b[0m', err);
    process.exit(1);
  }
} else if (command === 'sync') {
  const scriptsDir = path.join(process.cwd(), '.agent', 'scripts');
  const syncScript = path.join(scriptsDir, 'sync_memory.py');
  
  if (fs.existsSync(syncScript)) {
    console.log('Running Zenithgravity Memory Sync...');
    try {
        // Try to execute the python script
        execSync(`python3 ${syncScript}`, { stdio: 'inherit' });
    } catch (err) {
        // Fallback to 'python' if 'python3' is not mapped
        try {
            execSync(`python ${syncScript}`, { stdio: 'inherit' });
        } catch (fallbackErr) {
            console.error('Error executing sync_memory.py. Make sure Python is installed.');
            process.exit(1);
        }
    }
  } else {
    console.error('Error: .agent/scripts/sync_memory.py not found.');
    console.error('Did you run "npx zenithgravity init" in this project first?');
    process.exit(1);
  }
} else if (command === 'readme') {
  const readmePath = path.join(__dirname, '..', 'README.md');
  if (fs.existsSync(readmePath)) {
    const readmeContent = fs.readFileSync(readmePath, 'utf8');
    console.log('\n\x1b[1m\x1b[36m================ ZENITHGRAVITY-KIT README ================\x1b[0m\n');
    console.log(readmeContent);
    console.log('\n\x1b[1m\x1b[36m====================== END OF README =====================\x1b[0m\n');
  } else {
    console.error('Error: README.md not found.');
    process.exit(1);
  }
} else {
  console.error(`Unknown command: ${command}`);
  printHelp();
  process.exit(1);
}
