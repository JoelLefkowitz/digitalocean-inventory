const formatters = ["prettier", "black", "isort"];
const linters = ["cspell", "remark", "pylint", "bandit", "mypy"];

const exec = {
  bandit: "bandit -c .bandit -r builders",
  black: "black builders",
  cspell: "npx cspell -c .cspell.json '{*,.*,**/*}'",
  isort: "isort builders",
  mypy: "mypy builders",
  prettier: "prettier . --write",
  pylint: "pylint --rcfile .pylintrc builders",
  quickdocs: "quickdocs .quickdocs.yml",
  remark: "npx remark -r .remarkrc .",
  sphinx: "sphinx-build docs build",
  tox: "tox",
};

const execTask = (i) => "exec:".concat(i);

module.exports = function (grunt) {
  grunt.initConfig({ exec });
  grunt.loadNpmTasks("grunt-exec");
  grunt.registerTask("lint", linters.map(execTask));
  grunt.registerTask("format", formatters.map(execTask));
  grunt.registerTask("tests:unit", "exec:tox");
  grunt.registerTask("docs:generate", "exec:quickdocs");
  grunt.registerTask("docs:build", "exec:sphinx");
  grunt.registerTask("precommit", ["lint", "tests:unit", "docs:generate"]);
};
