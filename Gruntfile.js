module.exports = (grunt) => {
  grunt.initConfig({ exec });
  grunt.loadNpmTasks("grunt-exec");
  grunt.registerTask(
    "lint",
    "Lint the source code",
    toExecs(["cspell", "remark", "pylint", "bandit", "mypy"])
  );
  grunt.registerTask(
    "format",
    "Format the source code",
    toExecs(["prettier", "black", "isort", "autoflake"])
  );
  grunt.registerTask(
    "test",
    "Sequentially run all unit test suites",
    toExecs(["tox"])
  );
};

const toExecs = (arr) => arr.map((i) => "exec:".concat(i));

const flakeOptions = `
   -v -ri --exclude 'venv, conftest.py'
   --remove-unused-variables
   --remove-all-unused-imports
   --ignore-init-module-imports
`;

const exec = {
  autoflake: `autoflake . ${flakeOptions}`,
  bandit: "bandit -c .bandit -r src",
  black: "black .",
  cspell: 'npx cspell ".*" "*" "**/*"',
  isort: "isort .",
  mypy: "mypy . --exclude venv",
  prettier: "npx prettier . --write --ignore-path .gitignore",
  pylint: "pylint --rcfile .pylintrc  --fail-under=8 src tests",
  remark: "npx remark -r .remarkrc -i .gitignore . .github",
  tox: "tox . -e py",
};
