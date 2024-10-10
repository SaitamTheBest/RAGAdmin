module.exports = {
    extends: ['@commitlint/config-conventional'],
    rules: {
      'type-enum': [
        2,
        'always',
        [
          'feat',
          'fix',
          'chore',
          'docs',
          'style',
          'refactor',
          'perf',
          'test',
        ],
      ],
      'type-empty': [2, 'never'],
      'subject-empty': [2, 'never'],
    },
  };
  