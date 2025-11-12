CREATE TABLE "users" (
  "id" uud PRIMARY KEY,
  "username" text,
  "email" text,
  "password" text,
  "created_at" timestamp DEFAULT 'new()',
  "updated_at" timestamp DEFAULT 'new()'
);

CREATE TABLE "Places" (
  "id" uuid PRIMARY KEY,
  "name" text,
  "description" text,
  "features" text,
  "created_at" timestamp DEFAULT 'new()',
  "updated_at" timestamp DEFAULT 'new()'
);

CREATE TABLE "favorites" (
  "id" uuid PRIMARY KEY,
  "title" varchar,
  "user_id" uuid,
  "place_id" uuid,
  "created_at" timestamp DEFAULT 'now()',
  "updated_at" timestamp DEFAULT 'now()'
);

CREATE TABLE "Recommended_places" (
  "id" uuid PRIMARY KEY,
  "name" text,
  "description" text,
  "features" text,
  "created_at" timestamp DEFAULT 'new()',
  "updated_at" timestamp DEFAULT 'new()',
  "place_id" uuid
);

ALTER TABLE "favorites" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "favorites" ADD FOREIGN KEY ("place_id") REFERENCES "Places" ("id");

ALTER TABLE "Recommended_places" ADD FOREIGN KEY ("place_id") REFERENCES "Places" ("id");