SELECT a.* FROM article a
  LEFT JOIN comment c
    ON a.id = c.article_id
WHERE c.id ISNULL;